# app/routes/ai.py

from flask import Blueprint, request, jsonify, session
from app.model_factory import ModelFactory, GPT4Model, MistralModel

bp = Blueprint('ai', __name__)

# Dictionary to simulate available models
available_models = {
    "1": GPT4Model(),
    "2": MistralModel()
}
@bp.route('/analyze')
def analyze():
    return "AI Analysis Page"

@bp.route("/query", methods=["POST"])
def query_model():
    data = request.json
    user_tier = session.get("tier", "personal")  # Default to personal if not set
    selected_model_name = session.get("model")   # Model selected via /choose_model

    # Determine model to use
    if selected_model_name:
        # Use strategy pattern: apply model based on session state
        model = next((m for m in available_models.values()
                      if m.__class__.__name__ == selected_model_name), MistralModel())
    else:
        # Use factory pattern: get model based on tier
        model = ModelFactory.get_model(user_tier)
        session["model"] = model.__class__.__name__

    query_text = data.get("query", "")
    response = model.generate(query_text)

    return jsonify({
        "response": response,
        "model_used": model.__class__.__name__
    })


@bp.route("/choose_model", methods=["POST"])
def choose_model():
    choice = request.json.get("choice")  # Expecting "1" or "2"
    if choice in available_models:
        selected = available_models[choice].__class__.__name__
        session["model"] = selected
        return jsonify({"message": f"Model set to {selected}"})
    return jsonify({"error": "Invalid model choice"}), 400


@bp.route("/available_models", methods=["GET"])
def list_models():
    model_list = {
        "1": "GPT-4 (Corporate)",
        "2": "Mistral-7B (Personal)"
    }
    current = session.get("model", "Not selected")
    return jsonify({
        "available_models": model_list,
        "current_model": current
    })


@bp.route("/set_tier", methods=["POST"])
def set_tier():
    tier = request.json.get("tier")  # "corporate" or "personal"
    if tier in ["corporate", "personal"]:
        session["tier"] = tier
        session.pop("model", None)  # Reset model on tier change
        return jsonify({"message": f"User tier set to {tier}"})
    return jsonify({"error": "Invalid tier"}), 400
