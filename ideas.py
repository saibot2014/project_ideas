def show_ideas(ideas):
    for idea in ideas:
        print(f"Название: {idea['Название']}, Жанр: {idea['Жанр']}, Сложность: {idea['Сложность']}")
def add_idea(ideas, name, topic, difficulty):
    idea = {"Название": name, "Жанр": topic, "Сложность": difficulty}
    ideas.append(idea)