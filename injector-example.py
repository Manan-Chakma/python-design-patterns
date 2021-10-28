from injector import Injector, Module, provider, singleton, inject

# Example 1

class Api:
    def fetch_remote_data(self):
        print('Api called')
        return 42


# class BusinessLogic:
#
#     def __init__(self, api):
#         self.api = api
#
#     def do_stuff(self):
#         api_result = self.api.fetch_remote_data()
#         print(f"Api result is {api_result}")
#
#
# if __name__ == '__main__':
#     api = Api()
#     logic = BusinessLogic(api=api)
#     print(logic.do_stuff())

# Example - 2

class BusinessLogic:

    def __init__(self, api: Api):
        self.api = api

    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f"Api result is {api_result}")


"""
    Annotation and return types are must to provide
"""


class AppModule(Module):

    @singleton
    @provider
    def provide_business_logic(self, api: Api) -> BusinessLogic:
        print('provide business logic method gets called')
        return BusinessLogic(api=api)

    @singleton
    @provider
    def provide_api(self) -> Api:
        print("provide api method gets called")
        return Api()

    """
    if provide_api and provide_ultapalta method is given then provide_ultapalta method is getting called
    else the provide_api method gets called
    """
    # @singleton
    # @provider
    # def provide_ultapalta(self) -> Api:
    #     print("provide ultapalta method gets called")
    #     return Api()

    """
        Below method give error i.e. without return type gives an error
    """    # @singleton
    # @provider
    # def provide_ultapaltamalta(self):
    #     print("provide ultapaltamalta method gets called")
    #     return Api()


if __name__ == "__main__":
    injector = Injector(AppModule())
    logic = injector.get(BusinessLogic)
    logic.do_stuff()
