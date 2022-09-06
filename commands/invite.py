import random
import hikari
import tanjun

from constants import Constants

component = tanjun.Component()


@component.with_slash_command
@tanjun.as_slash_command(
    "invite",
    "Invite the CS-Pound Discord Bot to your own server.",
    default_to_ephemeral=True,
)
async def invite_command(ctx: tanjun.abc.Context) -> None:
    embed = hikari.Embed(
        title="Invite",
        description=f"Invite CS-Pound to your own server: https://haruyuki.moe/cs-pound/\nBot having problems? Report them here: {Constants.support_link} ",
        colour="#4ba139",
    )
    await ctx.respond(embed)


component = tanjun.Component().load_from_scope().make_loader()
