from app.gameimpl import x01_match


class ObjectFactory:
    def __init__(self):
        self.builders = {}

    def register_builder(self, key, builder, object_factory):
        self.builders[key] = builder
        factory = object_factory.ObjectFactory()
        factory.register_builder('X01', x01_match.X01MatchBuilder())
        x01 = factory.create('X01')

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)



