
class User(dict):
    def __init__(self, user_id, name, instruments, created_at, last_accessed):
        dict.__init__(self,
                      id=user_id,
                      name=name,
                      instruments=instruments,
                      created_at=created_at,
                      last_accessed=last_accessed)
        self.user_id = user_id
        self.name = name
        self.instruments = instruments
        self.created_at = created_at
        self.last_accessed = last_accessed


class Instrument(dict):
    def __init__(self, instrument_id, name, created_at, last_accessed):
        dict.__init__(self,
                      id=instrument_id,
                      name=name,
                      created_at=created_at,
                      last_accessed=last_accessed
                      )
        self.id = instrument_id
        self.name = name
        self.created_at = created_at
        self.last_accessed = last_accessed

