import json

import hikari
import tanjun


component = tanjun.Component()

help_list = {}
command_list = []
with open("help.json") as f:  # Open help.json
    help_list = json.load(f)  # Load the JSON data
for _, value in help_list["categories"].items():
    for command, _ in value["commands"].items():
        command_list.append(command.replace(" ", "").lower())


@component.with_slash_command
@tanjun.as_slash_command(
    "help",
    "Gives you information on usage and examples of the bot commands.",
    default_to_ephemeral=False,
)
async def help(ctx: tanjun.abc.Context) -> None:
    embed = hikari.Embed(colour=0x4BA139)  # Create empty embed

    if args == "" or args == "public":
        # Add Warning help information to embed
        title = f':{help_list["warning"]["icon"]}: __**Note**__'
        content = help_list["warning"]["description"] + "\n\n_"
        embed.add_field(name=title, value=content, inline=False)

        for category, category_data in help_list["categories"].items():
            title = f':{category_data["icon"]}: __**{category} Commands**__'
            content = (
                "\n".join(
                    [
                        f'`{example["usage"]}`'
                        for _, example in category_data["commands"].items()
                    ]
                )
                + "\n_"
            )
            embed.add_field(name=title, value=content, inline=False)

    else:
        if args in command_list:
            for key, value in help_list["categories"].items():
                for key2, value2 in value["commands"].items():
                    if args == key2.replace(" ", "").lower():
                        content = f'`{value2["usage"]}` - {value2["description"]}'  # `usage` - description
                        if value2["examples"]:  # If there are examples for the command
                            content += "\n\n*Examples:* \n" + "\n".join(
                                [
                                    "`" + value3 + "`"
                                    for key3, value3 in value2["examples"].items()
                                ]
                            )

                        if value2["aliases"]:  # If there are aliases for the command
                            content += "\n\n*Aliases:* " + ", ".join(
                                [
                                    "`" + value3 + "`"
                                    for key3, value3 in value2["aliases"].items()
                                ]
                            )  # *Aliases:* `alias1`, `alias2`, `alias3`
                        embed.add_field(name=key2, value=content, inline=False)
        else:
            await ctx.respond("That command doesn't exist!")
            return

    if args != "public" or public != "public":
        ctx.set_ephemeral_default(True)

    await ctx.respond(embed)


@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
