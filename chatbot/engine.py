from .data import faq_data


def get_response(user_input):

    user_input = user_input.lower()

    for key in faq_data:
        if key in user_input:
            return faq_data[key]

    return "Sorry, I didn't understand. Please contact support."