import openai

openai.api_key = "REPLACE_ME_WITH_YOUR_OPENAI_KEY"


def get_recipe(ingredients: list[str]):
    messages = [
        {
            "role": "system",
            "content": "You are a chef's assistant helping a chef come up with recipes with their leftovers.",
        }
    ]
    ingredient_msg = (
        "Please tell me a recipe that includes these ingredients: "
        + "\n".join(ingredients)
    )
    messages.append(
        {
            "role": "user",
            "content": ingredient_msg,
        },
    )

    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content

    return reply


def main():
    print("Welcome to the leftovers idea generator!")
    print(
        "Please enter an ingredient and optionally its quantity, like '1lb of ground beef' or 'broccoli'"
    )
    leftovers = []
    leftover = input(
        "Enter the leftover ingredient, or 'done' to finish adding leftovers: "
    )
    if leftover == "done":
        print(get_recipe(leftovers))
        exit(0)
    else:
        leftovers.append(leftover)
    while True:
        leftover = input(
            "Enter another ingredient, or 'done' to finish adding leftovers: "
        )
        if leftover == "done":
            break
        else:
            leftovers.append(leftover)

    print()
    print(get_recipe(leftovers))


if __name__ == "__main__":
    main()
