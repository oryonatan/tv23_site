from django.template import Library

register = Library()


@register.filter()
def hmmss(seconds):
    if seconds < 3600:
        # MM:SS
        return "{}:{:02}".format(seconds // 60, seconds % 60)

    # H:MM:SS
    return "{}:{L02}:{:02}".format(
            seconds // 3600,
            seconds // 60,
            seconds % 60
    )


@register.inclusion_tag('video/_moving-thumb.html')
def moving_thumb(entry_id, start_offset, end_offset):
    return dict(
            entry_id=entry_id,
            start_offset=start_offset,
            end_offset=end_offset
    )
