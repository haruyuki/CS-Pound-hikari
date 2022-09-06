import hikari
import tanjun
import chickensmoothie as cs

component = tanjun.Component()


@component.with_slash_command
@tanjun.as_slash_command(
    "time", "Show when the next opening is", default_to_ephemeral=False
)
async def time_command(ctx: tanjun.abc.Context) -> None:
    data = await cs.get_pound_string()
    opening_type = data[0]
    opening_string = data[1]
    embed = hikari.Embed(
        title=opening_type, description=opening_string, colour="#4ba139"
    )
    await ctx.respond(embed)


component = tanjun.Component().load_from_scope().make_loader()
