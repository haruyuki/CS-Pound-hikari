import aiohttp
import lxml.html
import textwrap
from urllib.parse import urlparse, parse_qs, parse_qsl

from constants import Constants
import functions


async def _get_web_data(link):  # Get web data from link
    success = False
    dom = None

    if "static" in link:  # If user provided direct link to pet image
        return success

    headers = {  # HTTP request headers
        "User-Agent": "CS Pound Discord Bot Agent "
        + Constants.version,  # Connecting User-Agent
        "From": Constants.contact_email,
    }
    parameters = {}
    components = urlparse(link)
    if components.query:
        parameters = dict(parse_qsl(components.query, keep_blank_values=True))

    base_link = f"{components.scheme}://{components.hostname}{components.path}"
    async with aiohttp.ClientSession() as session:  # Create an AIOHTTP session
        async with session.post(
            base_link, data=parameters, headers=headers
        ) as response:  # POST the variables to the base php link
            if response.status == 200:  # If received response is OK
                success = True
                connection = await response.text()  # Get text HTML of site
                dom = lxml.html.fromstring(connection)  # Convert into DOM
                dom.make_links_absolute("https://www.chickensmoothie.com")
    return success, dom


async def get_pound_string():
    data = await _get_web_data(
        "https://www.chickensmoothie.com/poundandlostandfound.php"
    )  # Get web data
    if data[0]:  # If the data is valid
        text = data[1].xpath("//h2/text()")  # Get all H2 elements in the data
        if text[0] == "Pound & Lost and Found":
            pound_type = text[0]
            text = f"Sorry, both the {pound_type} are closed at the moment."
        else:
            pound_type = text[0][4:]
            try:
                text = (
                    functions.multi_replace(
                        text[1],
                        {
                            "Sorry, the pound is closed at the moment.": "",
                            "Sorry, the Lost and Found is closed at the moment.": "",
                            "\n": "",
                            "\t": "",
                        },
                    )
                    + "."
                )  # Get opening text and remove extra formatting
            except IndexError:  # If there isn't any pound opening text
                text = f"""\
                {pound_type} is currently open!
                [Go {"claim an item" if pound_type == "Lost and Found" else "adopt a pet"} from the {pound_type}!](https://www.chickensmoothie.com/poundandlostandfound.php)"""
                text = textwrap.dedent(text)

        return pound_type, text
