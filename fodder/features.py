_feature_whens = dict()
_current_feature = ''
_current_feature_whens = dict()
_current_feature_stash = dict()
_listeners = dict()


def listen(event):
    """
    Annotation that allows methods to listen to events.
    :param event:
    :return:
    """

    def _listen(method):
        global _listeners
        if event not in _listeners:
            _listeners[event] = list()
        _listeners[event].append(method)
        return method

    return _listen


def feature(feature_name, *whens):
    global _feature_whens
    global _current_feature
    _current_feature = feature_name
    _feature_whens[feature_name] = dict()
    for w in whens:
        when_chain = dict()
        when_chain[w[0]] = w[1]
        _feature_whens[feature_name].update(when_chain)


def when(event_name, *next_steps):
    """
    Constructs tuples for use by `feature`
    :param event_name:
    :param next_steps:
    :return:
    """
    return event_name, next_steps


def start_feature(feature_name):
    global _feature_whens
    global _current_feature_whens
    global _current_feature_stash
    _current_feature_whens = _feature_whens.get(feature_name)
    _current_feature_stash = dict()  # for contextual data


def fire(event_name, *args, **kwargs):
    global _current_feature_whens
    global _current_feature
    global _listeners
    _current_feature_stash.update(**kwargs)
    listener_names = _current_feature_whens.get(event_name, ())
    for listener_name in listener_names:
        listeners = _listeners.get(listener_name)
        if listeners:
            for listener in listeners:
                listener(*args, stash=_current_feature_stash)
