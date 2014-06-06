from hoerapi.lowlevel import ApiResponse, call_api, parse_date
from hoerapi.CommonEqualityMixin import CommonEqualityMixin


class PodcastLive(CommonEqualityMixin):
    def __init__(self, data):
        self.id = data.get('id', 0)
        self.podcast = data.get('podcast', '')
        self.state = int(data.get('state', 0))
        self.type = int(data.get('type', 0))
        self.synced = int(data.get('synced', 0))
        self.title = data.get('title', '')
        self.url = data.get('url', '')
        self.streamurl = data.get('streamurl', '')
        self.livedate = parse_date(data.get('livedate', None))
        self.duration = int(data.get('duration', 0))
        self.twittered = data.get('twittered', '')


class PodcastLiveApiResponse(ApiResponse):
    def __init__(self, status, msg, events):
        ApiResponse.__init__(self, status, msg)

        self.events = []

        if events is not None:
            for pod in events:
                self.events.append(PodcastLive(pod))


def get_podcast_live(podcast, count=5):
    return call_api('getPodcastLive', PodcastLiveApiResponse, {
        'podcast': podcast,
        'count': count,
    })


class LiveByIDApiResponse(ApiResponse):
    def __init__(self, status, msg, data):
        ApiResponse.__init__(self, status, msg)

        self.data = None
        if data is not None and len(data) == 1:
            self.data = PodcastLive(data[0])


def get_live_by_id(id):
    return call_api('getLiveByID', LiveByIDApiResponse, { 'ID': id })


class LiveApiResponse(ApiResponse):
    def __init__(self, status, msg, events):
        ApiResponse.__init__(self, status, msg)

        self.events = []

        if events is not None:
            for pod in events:
                self.events.append(PodcastLive(pod))


def get_live(count=5, dateStart=None, dateEnd=None):
    params = { 'count': count }

    if dateStart is not None:
        params['dateStart'] = dateStart.strftime('%y-%m-%d')
    if dateEnd is not None:
        params['dateEnd'] = dateEnd.strftime('%y-%m-%d')

    return call_api('getLive', LiveApiResponse, params)