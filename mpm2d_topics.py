"""
mpm2d_topics.py
Curriculum-aligned MPM2D (Ontario Grade 10 Academic Math) Quadratic Topics
with step-by-step Manim scenes (9:16 vertical, zero-overlap) and voiceover scripts.
"""

from datetime import datetime, timezone
from typing import Dict, List, Optional, Any

TOPICS: List[Dict[str, Any]] = [
    {
        "id": "factoring_common_factor",
        "title": "Factoring by Common Factor (MPM2D)",
        "voiceover": (
            "Always check for a greatest common factor first! "
            "Take 6 x squared plus 9 x. "
            "Both terms divide by 3 x. "
            "Factor out 3 x, and divide each term: 6 x squared divided by 3 x is 2 x, "
            "and 9 x divided by 3 x is 3. "
            "So 6 x squared plus 9 x equals 3 x times 2 x plus 3!"
        ),
        "steps": [
            ("Expression", r"6x^2 + 9x", "#ffffff"),
            ("Find GCF", r"\text{GCF} = 3x", "#38bdf8"),
            ("Divide each term", r"3x\left(\frac{6x^2}{3x} + \frac{9x}{3x}\right)", "#34d399"),
            ("Factored Form", r"3x(2x + 3)", "#fbbf24"),
        ],
    },
    {
        "id": "factoring_grouping",
        "title": "Factoring by Grouping (MPM2D)",
        "voiceover": (
            "When you see four terms, try factoring by grouping! "
            "Group the first two terms and the last two terms. "
            "Factor x squared from the first pair to get x plus 3, "
            "and factor 2 from the second pair to also get x plus 3. "
            "Now factor out the common binomial x plus 3, giving x plus 3 times x squared plus 2!"
        ),
        "steps": [
            ("Four terms", r"x^3 + 3x^2 + 2x + 6", "#ffffff"),
            ("Group in pairs", r"(x^3 + 3x^2) + (2x + 6)", "#38bdf8"),
            ("Factor each pair", r"x^2(x + 3) + 2(x + 3)", "#34d399"),
            ("Factored Form", r"(x + 3)(x^2 + 2)", "#fbbf24"),
        ],
    },
    {
        "id": "factoring_sum_product",
        "title": "Factoring Simple Trinomials: Sum & Product (MPM2D)",
        "voiceover": (
            "To factor x squared plus 7 x plus 12, use sum and product! "
            "We need two numbers that multiply to 12 and add to 7. "
            "3 times 4 is 12, and 3 plus 4 is 7. "
            "So it factors directly into x plus 3 times x plus 4!"
        ),
        "steps": [
            ("Simple Trinomial", r"x^2 + 7x + 12", "#ffffff"),
            ("Product = 12, Sum = 7", r"3 \times 4 = 12,\quad 3 + 4 = 7", "#38bdf8"),
            ("Write factors", r"(x + 3)(x + 4)", "#fbbf24"),
        ],
    },
    {
        "id": "factoring_decomposition",
        "title": "Factoring by Decomposition (MPM2D)",
        "voiceover": (
            "When a is not 1, use decomposition! "
            "For 2 x squared plus 7 x plus 3, multiply a times c: 2 times 3 is 6. "
            "Find two numbers that multiply to 6 and add to 7: 6 and 1. "
            "Split 7 x into 6 x plus 1 x, then factor by grouping to get 2 x plus 1 times x plus 3!"
        ),
        "steps": [
            ("Complex Trinomial", r"2x^2 + 7x + 3", "#ffffff"),
            ("ac = 6, Sum = 7", r"6 \times 1 = 6,\quad 6 + 1 = 7", "#38bdf8"),
            ("Decompose bx", r"2x^2 + 6x + 1x + 3", "#34d399"),
            ("Group & Factor", r"2x(x + 3) + 1(x + 3)", "#34d399"),
            ("Factored Form", r"(2x + 1)(x + 3)", "#fbbf24"),
        ],
    },
    {
        "id": "factoring_special_product",
        "title": "Factoring Special Products: Difference of Squares (MPM2D)",
        "voiceover": (
            "Spot a difference of squares: a squared minus b squared! "
            "For 9 x squared minus 16, 9 x squared is 3 x all squared, and 16 is 4 squared. "
            "It factors into 3 x plus 4 times 3 x minus 4!"
        ),
        "steps": [
            ("Difference of Squares", r"9x^2 - 16", "#ffffff"),
            ("Rewrite as squares", r"(3x)^2 - (4)^2", "#38bdf8"),
            ("a^2 - b^2 = (a+b)(a-b)", r"(3x + 4)(3x - 4)", "#fbbf24"),
        ],
    },
    {
        "id": "solve_qe_factoring",
        "title": "Solve Quadratic Equations by Factoring (MPM2D)",
        "voiceover": (
            "To solve x squared minus 5 x plus 6 equals 0, factor first! "
            "Two numbers that multiply to 6 and add to negative 5 are negative 2 and negative 3. "
            "Set each factor equal to 0: x equals 2 or x equals 3!"
        ),
        "steps": [
            ("Equation", r"x^2 - 5x + 6 = 0", "#ffffff"),
            ("Factor", r"(x - 2)(x - 3) = 0", "#38bdf8"),
            ("Zero Product Property", r"x - 2 = 0 \quad \text{or} \quad x - 3 = 0", "#34d399"),
            ("Solutions", r"x = 2,\quad x = 3", "#fbbf24"),
        ],
    },
    {
        "id": "solve_qe_isolation",
        "title": "Solve Quadratic Equations by Isolation (MPM2D)",
        "voiceover": (
            "When there's no b x term, solve by isolation! "
            "For 2 x squared minus 18 equals 0, add 18 to both sides, then divide by 2 to get x squared equals 9. "
            "Take the square root of both sides—don't forget plus or minus! So x equals plus or minus 3."
        ),
        "steps": [
            ("Equation", r"2x^2 - 18 = 0", "#ffffff"),
            ("Isolate x^2", r"2x^2 = 18 \implies x^2 = 9", "#38bdf8"),
            ("Take Square Root", r"x = \pm\sqrt{9}", "#34d399"),
            ("Solutions", r"x = 3,\quad x = -3", "#fbbf24"),
        ],
    },
    {
        "id": "solve_qe_quadratic_formula",
        "title": "Solve Using the Quadratic Formula (MPM2D)",
        "voiceover": (
            "When a quadratic won't factor nicely, use the quadratic formula! "
            "x equals negative b plus or minus the square root of b squared minus 4 a c, all over 2 a. "
            "Plug in a, b, and c, simplify inside the root, and you get both roots!"
        ),
        "steps": [
            ("Standard Form", r"ax^2 + bx + c = 0", "#ffffff"),
            ("Quadratic Formula", r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", "#38bdf8"),
            ("Example: x^2 + 4x + 1 = 0", r"x = \frac{-4 \pm \sqrt{16 - 4}}{2}", "#34d399"),
            ("Simplified Roots", r"x = -2 \pm \sqrt{3}", "#fbbf24"),
        ],
    },
    {
        "id": "transformations_quadratic",
        "title": "Transformations of Quadratic Functions (MPM2D)",
        "voiceover": (
            "In vertex form y equals a times x minus h squared plus k, every letter transforms the parabola! "
            "a stretches, compresses, or reflects it. "
            "h shifts it left or right—remember, opposite sign! "
            "And k shifts it up or down."
        ),
        "steps": [
            ("Vertex Form", r"y = a(x - h)^2 + k", "#ffffff"),
            ("a: Vertical stretch/flip", r"a < 0 \implies \text{opens down}", "#38bdf8"),
            ("h: Horizontal shift", r"(x - h) \implies \text{shift right } h", "#34d399"),
            ("k: Vertical shift", r"+ k \implies \text{shift up } k", "#fbbf24"),
        ],
    },
    {
        "id": "axis_symmetry_factored",
        "title": "Axis of Symmetry from Factored Form (MPM2D)",
        "voiceover": (
            "In factored form y equals a times x minus r times x minus s, the x-intercepts are r and s. "
            "Because a parabola is symmetric, the axis of symmetry is halfway between them! "
            "Just average r and s: x equals r plus s divided by 2."
        ),
        "steps": [
            ("Factored Form", r"y = a(x - r)(x - s)", "#ffffff"),
            ("x-intercepts", r"x = r \quad \text{and} \quad x = s", "#38bdf8"),
            ("Midpoint Formula", r"x = \frac{r + s}{2}", "#fbbf24"),
        ],
    },
    {
        "id": "axis_symmetry_vertex",
        "title": "Axis of Symmetry from Vertex Form (MPM2D)",
        "voiceover": (
            "In vertex form y equals a times x minus h squared plus k, the vertex is h, k. "
            "The axis of symmetry always passes straight through the vertex, "
            "so its equation is simply x equals h!"
        ),
        "steps": [
            ("Vertex Form", r"y = a(x - h)^2 + k", "#ffffff"),
            ("Vertex", r"V(h, k)", "#38bdf8"),
            ("Axis of Symmetry", r"x = h", "#fbbf24"),
        ],
    },
    {
        "id": "axis_symmetry_standard",
        "title": "Axis of Symmetry from Standard Form (MPM2D)",
        "voiceover": (
            "In standard form y equals a x squared plus b x plus c, "
            "you can find the axis of symmetry directly using x equals negative b over 2 a! "
            "For example, if a is 2 and b is negative 8, x equals 8 over 4, which is 2."
        ),
        "steps": [
            ("Standard Form", r"y = ax^2 + bx + c", "#ffffff"),
            ("Axis of Symmetry", r"x = -\frac{b}{2a}", "#38bdf8"),
            ("Example: 2x^2 - 8x + 5", r"x = -\frac{-8}{2(2)} = 2", "#fbbf24"),
        ],
    },
    {
        "id": "expand_distributive",
        "title": "Expanding Binomials: Distributive Property (MPM2D)",
        "voiceover": (
            "To expand x plus 3 times x plus 5, use the distributive property! "
            "Multiply x by both terms in the second bracket, then multiply 3 by both terms. "
            "Combine like terms 5 x and 3 x to get x squared plus 8 x plus 15!"
        ),
        "steps": [
            ("Factored", r"(x + 3)(x + 5)", "#ffffff"),
            ("Distribute", r"x(x + 5) + 3(x + 5)", "#38bdf8"),
            ("Multiply", r"x^2 + 5x + 3x + 15", "#34d399"),
            ("Standard Form", r"x^2 + 8x + 15", "#fbbf24"),
        ],
    },
    {
        "id": "expand_area_model",
        "title": "Expanding Binomials: Area Model (MPM2D)",
        "voiceover": (
            "You can expand x plus 2 times x plus 4 using an area model! "
            "Split a rectangle into x and 2 along the top, and x and 4 along the side. "
            "Multiply each box: x squared, 4 x, 2 x, and 8. "
            "Add them up to get x squared plus 6 x plus 8!"
        ),
        "steps": [
            ("Dimensions", r"(x + 2)(x + 4)", "#ffffff"),
            ("4 Area Regions", r"x^2,\quad 4x,\quad 2x,\quad 8", "#38bdf8"),
            ("Sum Regions", r"x^2 + 4x + 2x + 8", "#34d399"),
            ("Standard Form", r"x^2 + 6x + 8", "#fbbf24"),
        ],
    },
    {
        "id": "expand_special_product",
        "title": "Expanding Special Products: Perfect Square (MPM2D)",
        "voiceover": (
            "Watch out for the common trap: x plus 3 all squared is NOT x squared plus 9! "
            "Use the perfect square pattern: a plus b squared equals a squared plus 2 a b plus b squared. "
            "So x plus 3 squared equals x squared plus 6 x plus 9!"
        ),
        "steps": [
            ("Perfect Square", r"(x + 3)^2", "#ffffff"),
            ("Pattern: (a+b)^2", r"a^2 + 2ab + b^2", "#38bdf8"),
            ("Substitute", r"x^2 + 2(x)(3) + 3^2", "#34d399"),
            ("Expanded", r"x^2 + 6x + 9", "#fbbf24"),
        ],
    },
    {
        "id": "discriminant_x_intercepts",
        "title": "Number of x-Intercepts Using the Discriminant (MPM2D)",
        "voiceover": (
            "How many x-intercepts does a quadratic have? Check the discriminant: b squared minus 4 a c! "
            "If it's positive, there are 2 x-intercepts. "
            "If it's zero, there is 1 x-intercept. "
            "If it's negative, there are 0 real x-intercepts!"
        ),
        "steps": [
            ("Discriminant", r"D = b^2 - 4ac", "#ffffff"),
            ("D > 0", r"2 \text{ x-intercepts}", "#34d399"),
            ("D = 0", r"1 \text{ x-intercept}", "#38bdf8"),
            ("D < 0", r"0 \text{ x-intercepts}", "#f87171"),
        ],
    },
    # Additional MPM2D Overall Expectations
    {
        "id": "completing_the_square",
        "title": "Completing the Square: Standard to Vertex Form (MPM2D)",
        "voiceover": (
            "To convert x squared plus 6 x plus 5 to vertex form, complete the square! "
            "Take half of 6, which is 3, and square it to get 9. "
            "Add and subtract 9 inside, factor the perfect square trinomial, and simplify to get x plus 3 squared minus 4!"
        ),
        "steps": [
            ("Standard Form", r"y = x^2 + 6x + 5", "#ffffff"),
            ("Half of 6, squared: 9", r"y = (x^2 + 6x + 9 - 9) + 5", "#38bdf8"),
            ("Factor & Simplify", r"y = (x + 3)^2 - 9 + 5", "#34d399"),
            ("Vertex Form", r"y = (x + 3)^2 - 4", "#fbbf24"),
        ],
    },
    {
        "id": "vertex_optimal_value",
        "title": "Finding Vertex & Max/Min Optimal Value (MPM2D)",
        "voiceover": (
            "In vertex form y equals negative 2 times x minus 3 squared plus 8, "
            "the vertex is 3, 8. "
            "Since a is negative, the parabola opens down, "
            "so it has a maximum value of 8 when x equals 3!"
        ),
        "steps": [
            ("Vertex Form", r"y = -2(x - 3)^2 + 8", "#ffffff"),
            ("Vertex", r"V(3, 8)", "#38bdf8"),
            ("a = -2 < 0", r"\text{Opens down} \implies \text{Maximum}", "#34d399"),
            ("Optimal Value", r"\text{Max } y = 8 \text{ at } x = 3", "#fbbf24"),
        ],
    },
    {
        "id": "equation_from_graph_vertex",
        "title": "Equation of a Quadratic from Vertex & Point (MPM2D)",
        "voiceover": (
            "Given vertex 2, negative 3 and a point 4, 5, start with vertex form! "
            "Plug in h equals 2 and k equals negative 3. "
            "Then substitute x equals 4 and y equals 5 to solve for a: 8 equals 4 a, so a equals 2!"
        ),
        "steps": [
            ("Vertex (2, -3)", r"y = a(x - 2)^2 - 3", "#ffffff"),
            ("Sub Point (4, 5)", r"5 = a(4 - 2)^2 - 3", "#38bdf8"),
            ("Solve for a", r"8 = 4a \implies a = 2", "#34d399"),
            ("Equation", r"y = 2(x - 2)^2 - 3", "#fbbf24"),
        ],
    },
    {
        "id": "graphing_step_pattern",
        "title": "Graphing Quadratics Using the Step Pattern (MPM2D)",
        "voiceover": (
            "To graph y equals 2 times x minus 1 squared minus 3 quickly, use the step pattern! "
            "Start at the vertex 1, negative 3. "
            "Multiply the basic step pattern 1, 3, 5 by a equals 2 to get 2, 6, 10. "
            "Step right 1, up 2; right 1, up 6!"
        ),
        "steps": [
            ("Vertex Form", r"y = 2(x - 1)^2 - 3", "#ffffff"),
            ("Start at Vertex", r"V(1, -3)", "#38bdf8"),
            ("Step Pattern (a=2)", r"2 \times (1, 3, 5) = (2, 6, 10)", "#fbbf24"),
        ],
    },
    {
        "id": "quadratic_word_problem_max_area",
        "title": "Quadratic Optimization: Max Area Word Problem (MPM2D)",
        "voiceover": (
            "A farmer has 40 meters of fencing for a rectangular pen. "
            "2 w plus l equals 40, so l equals 40 minus 2 w. "
            "Area equals w times 40 minus 2 w, which has zeros at 0 and 20. "
            "The maximum area happens halfway at w equals 10, giving 200 square meters!"
        ),
        "steps": [
            ("Constraint", r"2w + l = 40 \implies l = 40 - 2w", "#ffffff"),
            ("Area Function", r"A(w) = w(40 - 2w)", "#38bdf8"),
            ("Zeros: 0 and 20", r"w_{\max} = \frac{0 + 20}{2} = 10", "#34d399"),
            ("Max Area", r"A(10) = 10(20) = 200\text{ m}^2", "#fbbf24"),
        ],
    },
]


def pick_topic(topic_id: Optional[str] = None) -> Dict[str, Any]:
    """Return a specific topic by ID, or rotate automatically based on current UTC hour."""
    if topic_id:
        for t in TOPICS:
            if t["id"] == topic_id:
                return t
        raise ValueError(f"Unknown topic_id: {topic_id}")

    # Rotate every 6 hours (4 runs/day) through all 21 MPM2D topics
    now = datetime.now(timezone.utc)
    slot = int(now.timestamp() // (6 * 3600))
    return TOPICS[slot % len(TOPICS)]
