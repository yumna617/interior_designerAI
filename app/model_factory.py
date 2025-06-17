class BaseModel:
    def generate(self, query):
        raise NotImplementedError

class GPT4Model(BaseModel):
    def generate(self, query):
        return f"[GPT-4]: Processed '{query}'"

class MistralModel(BaseModel):
    def generate(self, query):
        return f"[Mistral-7B]: Processed '{query}'"

class ModelFactory:
    @staticmethod
    def get_model(tier):
        if tier == "corporate":
            return GPT4Model()
        return MistralModel()
