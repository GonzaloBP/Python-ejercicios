import re


class Extraccion_Email:

    emailRegex = re.compile(
        r"""(
        [a-zA-Z0-9._%+-]+   # username
        v @                 # @ symbol
        w [a-zA-Z0-9.-]+    # domain name
        (\.[a-zA-Z]{2,4})   # dot-something
        )""",
        re.VERBOSE,
    )

    def extracter_emails(self, a_file_handler):
        emails_encontrados = []
        for groups in emailRegex.findall(a_file_handler.read()):
            emails_encontrados.append(groups[0])
        return emails_encontrados

