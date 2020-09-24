import quizzservice

if __name__ == '__main__':
    api = quizzservice.QuizzWebServiceAPI()
    print(f"Antal frågor: {len(api.get_all_questions())}")
    #qs = quizzservice