from enum import Enum


class GovernmentType(Enum):
    DEMOCRACY = "Демократія"
    REPUBLIC = "Республіка"
    AUTOCRACY = "Автократія"
    CONSTITUTIONAL_MONARCHY = "Конституційна монархія"


class Country:
    def __init__(self, name="Невідомо", capital="Невідомо", code="N/A",
                 population=0, area=1.0, gdp=0.0,
                 government_type=GovernmentType.REPUBLIC, founded_year=1991):
        self.__name = name
        self.__capital = capital
        self.__code = code
        self.__population = population
        self.__area = area
        self.__gdp = gdp
        self.__government_type = government_type
        self.__founded_year = founded_year

    def __del__(self):
        print(f"[Деструктор] Країну '{self.__name}' видалено.")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_capital(self):
        return self.__capital

    def set_capital(self, capital):
        self.__capital = capital

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_population(self):
        return self.__population

    def set_population(self, population):
        self.__population = population

    def get_area(self):
        return self.__area

    def set_area(self, area):
        self.__area = area

    def get_gdp(self):
        return self.__gdp

    def set_gdp(self, gdp):
        self.__gdp = gdp

    def get_government_type(self):
        return self.__government_type

    def set_government_type(self, government_type):
        self.__government_type = government_type

    def get_founded_year(self):
        return self.__founded_year

    def set_founded_year(self, year):
        self.__founded_year = year

    def get_density(self):
        return self.__population / self.__area

    def display_info(self):
        print(f"Країна: {self.__name} ({self.__code}) | Столиця: {self.__capital} | ")
        print(f"Устрій: {self.__government_type.value} | Населення: {self.__population:,} | ")
        print(f"Площа: {self.__area:,.1f} км² | ВВП: ${self.__gdp:,.1f} млрд | ")
        print(f"Густина: {self.get_density():.2f} осіб/км²")


class Land:
    def __init__(self, name, hemisphere="Північна", countries=None):
        self.__name = name
        self.__hemisphere = hemisphere
        self.__countries = countries if countries is not None else []

    def __del__(self):
        print(f"[Деструктор] Материк '{self.__name}' видалено")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_hemisphere(self):
        return self.__hemisphere

    def set_hemisphere(self, hemisphere):
        self.__hemisphere = hemisphere

    def get_countries(self):
        return self.__countries

    def set_countries(self, countries):
        self.__countries = countries

    def add_country(self, country):
        self.__countries.append(country)

    def sort_by_gdp_and_show_top(self, top_n=3):
        sorted_countries = sorted(self.__countries, key=lambda c: c.get_gdp(), reverse=True)
        print(f"\n--- ТОП-{top_n} країн за ВВП на материку '{self.__name}' ---")
        for i, country in enumerate(sorted_countries[:top_n], start=1):
            print(f"{i}. {country.get_name()} — ВВП: ${country.get_gdp():,.1f} млрд")
        return sorted_countries

    def select_countries(self, min_population=50000000):
        selected = []
        for c in self.__countries:
            if c.get_population() >= min_population:
                selected.append(c)
        return selected

    def sort_by_release_date(self):
        return sorted(self.__countries, key=lambda c: c.get_founded_year())

    def display_info(self):
        print(f"\n=== Материк / Регіон: {self.__name} ({self.__hemisphere} півкуля) ===")
        print(f"Кількість країн: {len(self.__countries)}")
        for country in self.__countries:
            country.display_info()


def calculatePopulationDensity(*countries):
    print("\n--- Розрахунок густини населення ---")
    total_population = 0
    total_area = 0.0

    for c in countries:
        density = c.get_density()
        print(f"• {c.get_name()}: {density:.2f} осіб/км²")
        total_population += c.get_population()
        total_area += c.get_area()

    overall_density = total_population / total_area
    print(f"Загальна густина обраних країн: {overall_density:.2f} осіб/км²")
    return overall_density


def main():
    ukraine = Country("Україна", "Київ", "UA", 38000000, 603628.0, 178.8, GovernmentType.REPUBLIC, 1991)
    germany = Country("Німеччина", "Берлін", "DE", 84400000, 357592.0, 4456.0, GovernmentType.DEMOCRACY, 1949)
    uk = Country("Велика Британія", "Лондон", "GB", 67700000, 242495.0, 3340.0, GovernmentType.CONSTITUTIONAL_MONARCHY, 1707)
    poland = Country("Польща", "Варшава", "PL", 36800000, 312696.0, 811.2, GovernmentType.REPUBLIC, 1918)
    france = Country("Франція", "Париж", "FR", 68000000, 551695.0, 3031.0, GovernmentType.REPUBLIC, 1958)



    # Додавання до материка
    europe = Land("Європа", "Північна")
    for country in (ukraine, germany, uk, poland, france):
        europe.add_country(country)

    # Виведення інформації
    europe.display_info()

    for country in europe.get_countries():
        print(country.get_area())

    # Підрахунок густини
    calculatePopulationDensity(ukraine, poland, germany)

    # топ за ВВП
    # europe.sort_by_gdp_and_show_top(3)

    # print("\n--- Фільтрація (Населення >= 50,000,000) ---")
    # filtered = europe.select_countries(min_population=50000000)
    # for c in filtered:
    #     c.display_info()

    # print("\n--- Сортування за датою (роком) заснування ---")
    # for c in europe.sort_by_release_date():
    #     print(f"{c.get_name()} — {c.get_founded_year()} рік")


main()
