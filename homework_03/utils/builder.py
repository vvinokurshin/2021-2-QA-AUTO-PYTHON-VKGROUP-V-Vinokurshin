from dataclasses import dataclass

import faker

fake = faker.Faker()

class Builder:
    @staticmethod
    def segment(title=None):

        @dataclass
        class Segment:
            title: str = None

        if title is None:
            title = fake.lexify(text='??????? ??? ???')

        return Segment(title=title)
