from contextlib import redirect_stdout
import hikari
import io
import tanjun
import traceback
import textwrap

component = tanjun.Component()


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


@component.with_command
@tanjun.with_owner_check()
@tanjun.as_message_command("eval")
async def _eval(ctx: tanjun.abc.Context) -> None:
    # Retrieved and modified from https://github.com/vicky5124/robo-arc/blob/master/basic_python_bot_for_eval.py
    code = ctx.message.content[len(ctx.command.names[0]) + 2 :]

    if code.startswith("```") and code.endswith("```"):
        code = "\n".join(code.split("\n")[1:-1])
    else:
        code = code.strip("` \n")

    env = {
        "bot": ctx.client,
        "client": ctx.client,
        "msg": ctx.message,
        "message": ctx.message,
        "server_id": ctx.message.guild_id,
        "guild_id": ctx.message.guild_id,
        "channel_id": ctx.message.channel_id,
        "author": ctx.message.author,
        "eprint": eprint,
    }
    env.update(globals())
    stdout = io.StringIO()

    new_forced_async_code = f"async def code():\n{textwrap.indent(code, '    ')}"

    try:
        exec(
            new_forced_async_code, env
        )  # shut up pylint with "[exec-used] Use of exec [W0122]"
    except Exception as error:  # shut up pylint with "[broad-except] Catching too general exception Exception [W0703]"
        embed = hikari.Embed(
            title="Failed to execute.",
            description=f"{error} ```py\n{traceback.format_exc()}\n```\n```py\n{error.__class__.__name__}\n```",
            colour=(255, 10, 40),
        )
        await ctx.respond(embed=embed)
        await ctx.message.add_reaction("❌")
        return

    code = env["code"]

    try:
        with redirect_stdout(stdout):
            result = await code()
    except Exception as error:  # shut up pylint with "[broad-except] Catching too general exception Exception [W0703]"
        value = stdout.getvalue()
        embed = hikari.Embed(
            title="Failed to execute.",
            description=f"{error} ```py\n{traceback.format_exc()}\n```\n```py\n{value}\n```",
            colour=(255, 10, 40),
        )
        await ctx.respond(embed=embed)
        await ctx.message.add_reaction("\u274C")  # ❌
        return

    value = stdout.getvalue()
    embed = hikari.Embed(
        title="Success!",
        description=f"Returned value: ```py\n{result}\n```\nStandard Output: ```py\n{value}\n```",
        colour=(5, 255, 70),
    )
    await ctx.respond(embed=embed)
    await ctx.message.add_reaction("\u2705")  # ✅


@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
