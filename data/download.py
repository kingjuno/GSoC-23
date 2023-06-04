import gdown

MODELS = {
    "Model-1": {
        "train": "https://drive.google.com/file/d/1QMVLpqag6S9JWqzmGM_pK4C0F1eBVIfV/view?usp=sharing",
        "test": "https://drive.google.com/file/d/1rUAKLLS3p9jDaL9R9m84JVKvMcUuVsO1/view?usp=sharing",
    },
    "Model-2": {
        "train": "https://drive.google.com/file/d/1HYPkdtVUj9xsoGzFDxT4rhl37KmqDCg4/view?usp=sharing",
        "test": "https://drive.google.com/file/d/1PFdpqk7XOAKtg0Cnav4HTzyJiudx9dZv/view?usp=sharing",
    },
    "Model-3": {
        "train": "https://drive.google.com/file/d/1ynKMJoEeKKJqLfuKRR1Y7rQjeBMM0w94/view?usp=sharing",
        "test": "https://drive.google.com/file/d/18BuCv40t6qmiNnhjJF1y9rqSBhBOfDon/view?usp=sharing",
    },
    "Model-4": {},
}


def shareable_link_to_url(link):
    base = "https://drive.google.com/uc?id="
    id = link.split("/")[-2]
    return base + id


def main(args):
    model = args["model"]  # [TODO] to arg parser
    if model not in MODELS:
        print("Model not found")
        return

    model = MODELS[model]
    train_link = model["train"]
    test_link = model["test"]
    train_url = shareable_link_to_url(train_link)
    print(train_url)

    test_url = shareable_link_to_url(test_link)
    print(test_url)

    gdown.download(
        train_url, output="data/", quiet=False
    )


print(main({"model": "Model-1"}))
