


events = {}


def register_event(event: str, function: callable):
    handlers = events.get(event)

    if handlers is None:
        events[event] = [function]
    else:
        handlers.append(function)


def dispatch(event: str, data):
    handlers = events.get(event)
    print(event)
    if event is None:
        raise ValueError(f"Event {event} was not found")
    for  handler in handlers:
        handler(data)

