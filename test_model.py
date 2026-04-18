import numpy as np
from model import train_and_predict, get_accuracy

def test_predictions_not_none():
    #Test 1: Sprawdza, czy otrzymujemy jakąkolwiek predykcję.
    preds = train_and_predict()
    assert preds is not None, "Predictions should not be None."

def test_predictions_length():
    """
    Test 2:
    Sprawdza, czy długość listy predykcji jest większa od 0
    i czy odpowiada przewidywanej liczbie próbek testowych.
    Dla Iris: 150 próbek, test_size=0.2, więc zbiór testowy ma 30 próbek.
    """
    preds = train_and_predict()
    assert len(preds) > 0, "Predictions list should not be empty."
    assert len(preds) == 30, f"Expected 30 predictions, got {len(preds)}."

def test_predictions_value_range():
    """
    Test 3:
    Sprawdza, czy wartości w predykcjach mieszczą się w spodziewanym zakresie.
    Dla zbioru Iris mamy 3 klasy: 0, 1, 2.
    """
    preds = train_and_predict()
    valid_classes = {0, 1, 2}
    assert all(pred in valid_classes for pred in preds), \
        f"Predictions contain values outside expected classes: {preds}"

def test_model_accuracy():
    """
    Test 4:
    Sprawdza, czy model osiąga co najmniej 70% dokładności.
    """
    acc = get_accuracy()
    assert acc >= 0.7, f"Model accuracy too low: {acc}"