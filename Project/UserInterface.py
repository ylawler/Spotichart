import pycountry


class UserInterface():

    def __init__(self):
        self._country = None
        self.recurrence = None
        self.country_code = None
        self._num_retries = 0

    def get_country_code(self, country):

        # If the beginning of the country contains 'the' remove it and update the user_country input
        if country[:4].lower() == 'the ':
            country = country[3:].strip(' ')

        # returns the country code
        get_by_name = pycountry.countries.get(name=country.title())
        get_by_alpha_2 = pycountry.countries.get(alpha_2=country.upper())
        get_by_alpha_3 = pycountry.countries.get(alpha_3=country.upper())

        # print(get_by_name, get_by_alpha_3, get_by_official_name)

        if get_by_name is not None:
            return get_by_name.alpha_2.lower()
        elif get_by_alpha_2 is not None:
            return get_by_alpha_2.alpha_2.lower()
        elif get_by_alpha_3 is not None:
            return get_by_alpha_3.alpha_2.lower()
        elif country.lower() == "global":
            return "global"
        else:
            return None

    def get_user_input(self):
        print('Please enter the country:')
        # Get the country from the user
        valid_country = False
        self._num_retries = 0
        while not valid_country:
            user_country = input()

            # check if the country is valid
            if self.get_country_code(user_country) is not None:
                self._country = user_country
                self.country_code = self.get_country_code(user_country)
                valid_country = True
            else:
                print('Please Input a valid country!')
                self._num_retries += 1

        # Get the recurrence from the user
        print('Do you want the daily or weekly charts?')
        valid_recurrence = False
        while not valid_recurrence:
            user_recurrence = input()
            if user_recurrence.lower() == "daily" or user_recurrence.lower() == "weekly":
                self.recurrence = user_recurrence
                valid_recurrence = True
            else:
                print('Please enter: daily or weekly')
                self._num_retries += 1

