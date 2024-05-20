from flask import Blueprint, jsonify
from label_service import get_all_labels, predict_no_resnet, predict_resnet
from flask import request

label_bp = Blueprint('label_bp', __name__)


@label_bp.route('/api/labels/list', methods=['GET'])
def get_labels():
    labels = get_all_labels()
    return jsonify([label.to_dict() for label in labels])


@label_bp.route('/api/labels/predict/no-resnet', methods=['POST'])
def get_predict_no_resnet():
    image_file = check_request(request)
    result = predict_no_resnet(image_file)
    return result, 200


@label_bp.route('/api/labels/predict/resnet', methods=['POST'])
def get_predict_resnet():
    image_file = check_request(request)
    result = predict_resnet(image_file)
    return result, 200


def check_request(request):
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400

    image_file = request.files['image']

    if image_file.filename == '':
        return jsonify({'error': 'No selected image file'}), 400

    return image_file
