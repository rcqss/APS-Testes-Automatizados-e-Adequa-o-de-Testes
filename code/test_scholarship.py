import pytest
from ScholarshipEligibilityEvaluator import evaluate_scholarship, Status

#testes funcionais
def test_aprovado_caso_padrao():

    result = evaluate_scholarship(18, 8.5, 92.0, True, False)
    assert result.status == Status.APPROVED

@pytest.mark.parametrize("idade, gpa, presenca, cursos, registro, motivo_esperado", [
    (15, 9.0, 90.0, True, False, "aplicante é mais novo que a idade mínima."),
    (20, 5.5, 90.0, True, False, "gpa esta abaixo do minimo exigido."),
    (20, 9.0, 70.0, True, False, "frequencia esta abaixo do minimo exigido."),
    (20, 9.0, 90.0, False, False, "cursos requeridos nao foram concluidos."),
    (20, 9.0, 90.0, True, True, "aplicante tem registro disciplinar."),
])
def test_casos_rejeitados(idade, gpa, presenca, cursos, registro, motivo_esperado):

    result = evaluate_scholarship(idade, gpa, presenca, cursos, registro)
    assert result.status == Status.REJECTED

@pytest.mark.parametrize("idade, gpa, presenca", [
    (17, 8.0, 90.0), 
    (20, 6.5, 90.0),
    (20, 8.0, 78.0),
])
def test_casos_revisao_manual(idade, gpa, presenca):
    result = evaluate_scholarship(idade, gpa, presenca, True, False)
    assert result.status == Status.MANUAL_REVIEW

#testes de valor limite

@pytest.mark.parametrize("gpa, status_esperado", [
    (6.0, Status.MANUAL_REVIEW),
    (7.0, Status.APPROVED),
])
def test_valores_limite_gpa(gpa, status_esperado):
    result = evaluate_scholarship(20, gpa, 90.0, True, False)
    assert result.status == status_esperado

#testes de entrada invalida

def test_gpa_invalido():
    with pytest.raises(ValueError):
        evaluate_scholarship(20, 11.0, 90.0, True, False)

def test_presenca_invalida():
    with pytest.raises(ValueError):
        evaluate_scholarship(20, 8.0, 150.0, True, False)