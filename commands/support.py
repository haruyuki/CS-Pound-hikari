import random
import hikari
import tanjun

component = tanjun.Component()


@component.with_command
@tanjun.as_message_command("support")
async def command_support(ctx: tanjun.abc.Context) -> None:
    await ctx.author.send("Link to support server")
    embed = hikari.Embed(
        title="Support", description="PM Successful!", colour="#4ba139"
    )
    await ctx.respond(embed)


@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
