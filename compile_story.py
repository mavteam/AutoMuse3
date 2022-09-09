import os


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


if __name__ == '__main__':
    files = [i for i in os.listdir('logs/') if 'summary' not in i]
    result = list()
    for file in files:
        result.append(open_file('logs/%s' % file))
    text = '\n'.join(result)
    save_file('story.txt', text)