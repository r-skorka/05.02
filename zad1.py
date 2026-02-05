import unittest


def analyze_grades(text: str) -> dict:
   # """
   # Analizuje tekst z ocenami
   # >>> analyze_grades("3 3 3")
   # {'count': 3, 'avg': 3.0, 'best': 3, 'worst': 3}
   # """
    parts = text.split()
    if not parts:
        raise ValueError("No grades provided")

    grades = []
    for p in parts:
        if not p.isdigit():
            raise ValueError("Grades must be integers")
        g = int(p)
        if g < 1 or g > 5:
            raise ValueError("Grades must be in range 1..5")
        grades.append(g)

    return {
        "count": len(grades),
        "avg": sum(grades) / len(grades),
        "best": max(grades),
        "worst": min(grades)
    }

# unittest, pytest, doctest, selenium

class TestAnalyzeGrades(unittest.TestCase):
    def test_correct_data(self):
        result = analyze_grades("5 4 3 2")
        self.assertEqual(result["count"], 4)
        self.assertEqual(result["avg"], 3.5)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            analyze_grades("")

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            analyze_grades("1 3 6")

    def test_single_grade(self):
        expected = {"count": 1, "avg": 3.0, "best": 3, "worst": 3}
        self.assertEqual(analyze_grades("3"), expected)

if __name__ == "__main__":
    unittest.main()
