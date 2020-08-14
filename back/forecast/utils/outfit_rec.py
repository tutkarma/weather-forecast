import json

'''
wind_spd --- скорость ветра м/с [0 100]
app_temp --- температура по ощущениям [-50 50]
clouds --- облачность  (%) [0-100]
rh --- относительная влажность воздуха (%) [0-100]
'''

class RecSysOutfit:
    def __init__(self, outfit_path, scores_path):
        self.knowledge_base = self._get_knowledge_base(
            outfit_path, scores_path)

    def get_recomendation(self, weather):
        wind_spd = weather['wind_spd']
        app_temp = weather['app_temp']
        clouds = weather['clouds']
        rh = weather['rh']

        s = self.score(self.f_temp(app_temp),
                  self.f_rh(rh),
                  self.f_wind(wind_spd),
                  self.f_clouds(clouds))

        rec = 'Recommendation not found'
        for item, v in self.knowledge_base.items():
            start, end = v['start'], v['end']
            if start < s <= end:
                rec = item
                break
        return rec

    def f_temp(self, x):
        y = 100
        if -20 < x <= -15:
            y = 90
        elif -15 < x <= -10:
            y = 80
        elif -10 < x <= -5:
            y = 70
        elif -5 < x <= 0:
            y = 60
        elif 0 < x <= 5:
            y = 50
        elif 5 < x <= 10:
            y = 40
        elif 10 < x <= 15:
            y = 30
        elif 15 < x <= 20:
            y = 20
        elif 20 < x <= 25:
            y = 10
        else:
            y = 0
        return y

    def f_rh(self, x):
        y = 0
        if 50 < x <= 60:
            y = 20
        elif 60 < x <= 70:
            y = 40
        elif 70 < x <= 80:
            y = 60
        elif 80 < x <= 90:
            y = 80
        else:
            y = 100
        return y

    def f_wind(self, x):
        y = 0
        if 0.5 < x <= 1.5:
            y = 20
        elif 1.5 < x <= 2.5:
            y = 40
        elif 2.5 < x <= 3.5:
            y = 60
        elif 3.5 < x <= 4.5:
            y = 80
        else:
            y = 100
        return y

    def f_clouds(self, x):
        return x

    def score(self, x1, x2, x3, x4):
        return 0.5 * x1 + 0.5 * x2 + 0.2 * x3 + 0.2 * x4

    def _get_knowledge_base(self, outfit_path, scores_path):
        with open(outfit_path, 'r') as f:
            outfit = json.load(f)

        with open(scores_path, 'r') as f:
            scores = json.load(f)

        data = {}

        for key in outfit:
            data[outfit[key]] = scores[key]

        return data
