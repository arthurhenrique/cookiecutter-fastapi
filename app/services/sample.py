

class SampleBusiness:
    dataset = None

    def __init__(self, dataset, *args, **kwargs):
        self.dataset = dataset

    def get_sample(self):
        return [
            x
            for x in self.dataset
            if (
                True
            )
        ]


    def update(self):
        _ = [
            i.update(
                name="CHANGED"
            )
            for i in self.dataset
            if i["id"] == 5
        ]

        return self.dataset


def get_sample(data):

    dataset = []
    sample = SampleBusiness(data)

    dataset += sample.get_sample()
    dataset += sample.update()

    return data
