import hikari
import tanjun
import chickensmoothie as cs

component = tanjun.Component()


@tanjun.as_slash_command(
    "time", "Show when the next opening is", default_to_ephemeral=False
)
async def time(ctx: tanjun.abc.Context) -> None:
    data = await cs.get_pound_string()
    opening_type = data[0]
    opening_string = data[1]
    embed = hikari.Embed(
        title=opening_type, description=opening_string, colour="#4ba139"
    )
    await ctx.respond(embed)


@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
