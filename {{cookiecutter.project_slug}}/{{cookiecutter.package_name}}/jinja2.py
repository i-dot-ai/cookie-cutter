import jinja2
from django.templatetags.static import static
from django.urls import reverse
from markdown_it import MarkdownIt

markdown_converter = MarkdownIt("js-default")


def url(path, *args, **kwargs):
    assert not (args and kwargs)
    return reverse(path, args=args, kwargs=kwargs)


def markdown(text, cls=None):
    """
    Converts the given text into markdown.
    The `replace` statement replaces the outer <p> tag with one that contains the given class, otherwise the markdown
    ends up double wrapped with <p> tags.
    Args:
        text: The text to convert to markdown
        cls (optional): The class to apply to the outermost <p> tag surrounding the markdown

    Returns:
        Text converted to markdown
    """
    html = markdown_converter.render(text).strip()
    html = html.replace("<p>", f'<p class="{cls or ""}">', 1).replace("</p>", "", 1)
    return html


def environment(**options):
    extra_options = dict()
    env = jinja2.Environment(  # nosec B701
        **{
            "autoescape": True,
            **options,
            **extra_options,
        }
    )
    env.globals.update(
        {
            "static": static,
            "url": url,
        }
    )
    return env
