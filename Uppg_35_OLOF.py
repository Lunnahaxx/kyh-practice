import quizzservice

if __name__ == 'main':
    api = quizzservice.QuizzWebServiceAPI()
    print(f"Antal frågor: {api.get_all_questions()}")
    #qs = quizzservice