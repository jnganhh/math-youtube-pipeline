"""
mpm2d_topics.py
Curriculum-aligned MPM2D (Ontario Grade 10 Academic Math) Quadratic Topics.
Each topic uses segmented narration for 100% frame-accurate audio-video sync
and a dedicated visual mode ('graph', 'area', or 'algebra') in a clean white/light theme.
"""

from datetime import datetime, timezone
from typing import Dict, List, Optional, Any

TOPICS: List[Dict[str, Any]] = [
    {
        "id": "factoring_common_factor",
        "title": "Factoring by Common Factor",
        "subtitle": "MPM2D • Always Check GCF First",
        "visual": "algebra",
        "rule": r"\text{GCF}(a, b)\left(\frac{a}{\text{GCF}} + \frac{b}{\text{GCF}}\right)",
        "segments": [
            {
                "narration": "Welcome to M P M 2 D! Before using any fancy factoring trick, always check for a greatest common factor first.",
                "label": "Golden Rule",
                "tex": r"\text{Always factor out the GCF first!}",
                "color": "#2563eb",
            },
            {
                "narration": "Let's factor 6 x squared plus 9 x. Look at the numbers 6 and 9: the largest number that divides both is 3.",
                "label": "Example 1",
                "tex": r"6x^2 + 9x",
                "color": "#0f172a",
            },
            {
                "narration": "Both terms also share an x, so our greatest common factor is 3 x.",
                "label": "Find GCF",
                "tex": r"\text{GCF}(6x^2, 9x) = 3x",
                "color": "#2563eb",
            },
            {
                "narration": "Write 3 x in front, and divide each term by 3 x. 6 x squared divided by 3 x is 2 x, and 9 x divided by 3 x is 3.",
                "label": "Divide Each Term",
                "tex": r"3x\left(\frac{6x^2}{3x} + \frac{9x}{3x}\right) = 3x(2x + 3)",
                "color": "#059669",
            },
            {
                "narration": "Now try one yourself: factor 10 x squared minus 15 x. Pause and find the G C F.",
                "label": "Try It Yourself",
                "tex": r"10x^2 - 15x",
                "color": "#0f172a",
            },
            {
                "narration": "The G C F of 10 x squared and 15 x is 5 x. Dividing both terms gives 5 x times 2 x minus 3!",
                "label": "Solution",
                "tex": r"5x(2x - 3)",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "factoring_grouping",
        "title": "Factoring by Grouping",
        "subtitle": "MPM2D • Four-Term Expressions",
        "visual": "algebra",
        "rule": r"a(x + y) + b(x + y) = (x + y)(a + b)",
        "segments": [
            {
                "narration": "When you see four terms with no single common factor, use factoring by grouping!",
                "label": "When to Use",
                "tex": r"4\text{ terms} \implies \text{Group in pairs}",
                "color": "#2563eb",
            },
            {
                "narration": "Let's factor x cubed plus 3 x squared plus 2 x plus 6. Pair the first two terms and the last two terms.",
                "label": "Group Pairs",
                "tex": r"(x^3 + 3x^2) + (2x + 6)",
                "color": "#0f172a",
            },
            {
                "narration": "Factor x squared from the first pair to get x plus 3, and factor 2 from the second pair to also get x plus 3.",
                "label": "Factor Each Pair",
                "tex": r"x^2(x + 3) + 2(x + 3)",
                "color": "#059669",
            },
            {
                "narration": "Notice the matching bracket x plus 3! Factor it out to get x plus 3 times x squared plus 2.",
                "label": "Factored Form",
                "tex": r"(x + 3)(x^2 + 2)",
                "color": "#d97706",
            },
            {
                "narration": "Try this one: factor x cubed minus 4 x squared plus 5 x minus 20.",
                "label": "Try It Yourself",
                "tex": r"x^3 - 4x^2 + 5x - 20",
                "color": "#0f172a",
            },
            {
                "narration": "Pull x squared from the first pair and 5 from the second pair to get x minus 4 times x squared plus 5!",
                "label": "Solution",
                "tex": r"(x - 4)(x^2 + 5)",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "factoring_sum_product",
        "title": "Factoring Simple Trinomials",
        "subtitle": "MPM2D • Sum & Product",
        "visual": "area",
        "area_labels": ["x", "+3", "x", "+4", "x^2", "4x", "3x", "12"],
        "rule": r"x^2 + (p+q)x + pq = (x + p)(x + q)",
        "segments": [
            {
                "narration": "To factor a simple trinomial like x squared plus 7 x plus 12, look at the area model of a rectangle!",
                "label": "Example 1",
                "tex": r"x^2 + 7x + 12",
                "color": "#0f172a",
            },
            {
                "narration": "We need two numbers that multiply to 12 and add to 7. 3 times 4 is 12, and 3 plus 4 is 7.",
                "label": "Product = 12, Sum = 7",
                "tex": r"3 \times 4 = 12,\quad 3 + 4 = 7",
                "color": "#2563eb",
            },
            {
                "narration": "On our area grid, x squared, 3 x, 4 x, and 12 form a rectangle with sides x plus 3 and x plus 4.",
                "label": "Factored Form",
                "tex": r"(x + 3)(x + 4)",
                "color": "#059669",
            },
            {
                "narration": "Try one with negatives: factor x squared minus 2 x minus 15.",
                "label": "Try It Yourself",
                "tex": r"x^2 - 2x - 15",
                "color": "#0f172a",
            },
            {
                "narration": "Negative 5 times 3 is negative 15, and negative 5 plus 3 is negative 2. So we get x minus 5 times x plus 3!",
                "label": "Solution",
                "tex": r"(x - 5)(x + 3)",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "factoring_decomposition",
        "title": "Factoring by Decomposition",
        "subtitle": "MPM2D • Complex Trinomials (a ≠ 1)",
        "visual": "area",
        "area_labels": ["2x", "+1", "x", "+3", "2x^2", "6x", "1x", "3"],
        "rule": r"ax^2 + bx + c \rightarrow \text{split } bx \text{ using } ac",
        "segments": [
            {
                "narration": "When a is not 1, like 2 x squared plus 7 x plus 3, use decomposition and the area model!",
                "label": "Example 1",
                "tex": r"2x^2 + 7x + 3",
                "color": "#0f172a",
            },
            {
                "narration": "Multiply a times c: 2 times 3 equals 6. Find two numbers that multiply to 6 and add to 7: 6 and 1.",
                "label": "ac = 6, Sum = 7",
                "tex": r"6 \times 1 = 6,\quad 6 + 1 = 7",
                "color": "#2563eb",
            },
            {
                "narration": "Split 7 x into 6 x and 1 x in our area boxes, then factor out the greatest common factor of each row and column.",
                "label": "Decompose & Group",
                "tex": r"2x(x + 3) + 1(x + 3)",
                "color": "#059669",
            },
            {
                "narration": "The sides of the rectangle give us 2 x plus 1 times x plus 3!",
                "label": "Factored Form",
                "tex": r"(2x + 1)(x + 3)",
                "color": "#d97706",
            },
            {
                "narration": "Try one yourself: factor 3 x squared plus 10 x plus 8. Remember: a times c is 24.",
                "label": "Try It Yourself",
                "tex": r"3x^2 + 10x + 8",
                "color": "#0f172a",
            },
            {
                "narration": "6 and 4 multiply to 24 and add to 10. Factoring by grouping gives 3 x plus 4 times x plus 2!",
                "label": "Solution",
                "tex": r"(3x + 4)(x + 2)",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "factoring_special_product",
        "title": "Factoring Special Products",
        "subtitle": "MPM2D • Difference of Squares",
        "visual": "area",
        "area_labels": ["3x", "+4", "3x", "-4", "9x^2", "-12x", "+12x", "-16"],
        "rule": r"a^2 - b^2 = (a + b)(a - b)",
        "segments": [
            {
                "narration": "Spot a difference of squares: two perfect squares separated by a minus sign, like 9 x squared minus 16.",
                "label": "Example 1",
                "tex": r"9x^2 - 16",
                "color": "#0f172a",
            },
            {
                "narration": "9 x squared is 3 x all squared, and 16 is 4 squared. Notice in the area model, plus 12 x and minus 12 x cancel out!",
                "label": "Rewrite as Squares",
                "tex": r"(3x)^2 - (4)^2",
                "color": "#2563eb",
            },
            {
                "narration": "So it factors cleanly into 3 x plus 4 times 3 x minus 4.",
                "label": "Factored Form",
                "tex": r"(3x + 4)(3x - 4)",
                "color": "#059669",
            },
            {
                "narration": "Try this one: factor 25 x squared minus 49.",
                "label": "Try It Yourself",
                "tex": r"25x^2 - 49",
                "color": "#0f172a",
            },
            {
                "narration": "5 x squared minus 7 squared factors into 5 x plus 7 times 5 x minus 7!",
                "label": "Solution",
                "tex": r"(5x + 7)(5x - 7)",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "solve_qe_factoring",
        "title": "Solve Quadratics by Factoring",
        "subtitle": "MPM2D • Zero Product Property",
        "visual": "graph",
        "graph": {
            "x_range": [-4, 6, 1],
            "y_range": [-6, 8, 2],
            "curves": [{"a": 1, "h": 2.5, "k": -0.25, "color": "#2563eb", "label": "y = x^2 - 5x + 6"}],
            "dots": [[2, 0, "#059669", "(2, 0)"], [3, 0, "#059669", "(3, 0)"]],
        },
        "rule": r"AB = 0 \implies A = 0 \text{ or } B = 0",
        "segments": [
            {
                "narration": "Solving a quadratic equation means finding where the parabola crosses the x-axis, where y equals 0.",
                "label": "Equation",
                "tex": r"x^2 - 5x + 6 = 0",
                "color": "#0f172a",
            },
            {
                "narration": "First, factor the left side: negative 2 and negative 3 multiply to 6 and add to negative 5.",
                "label": "Factor",
                "tex": r"(x - 2)(x - 3) = 0",
                "color": "#2563eb",
            },
            {
                "narration": "By the Zero Product Property, set each bracket to 0. That gives x equals 2 and x equals 3—right at the two green dots on the graph!",
                "label": "x-Intercepts / Roots",
                "tex": r"x = 2,\quad x = 3",
                "color": "#059669",
            },
            {
                "narration": "Try one yourself: solve x squared plus 3 x minus 10 equals 0.",
                "label": "Try It Yourself",
                "tex": r"x^2 + 3x - 10 = 0",
                "color": "#0f172a",
            },
            {
                "narration": "It factors into x plus 5 times x minus 2 equals 0, giving x equals negative 5 and x equals 2!",
                "label": "Solution",
                "tex": r"x = -5,\quad x = 2",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "solve_qe_isolation",
        "title": "Solve Quadratics by Isolation",
        "subtitle": "MPM2D • Don't Forget ±",
        "visual": "graph",
        "graph": {
            "x_range": [-5, 5, 1],
            "y_range": [-10, 8, 2],
            "curves": [{"a": 1, "h": 0, "k": -9, "color": "#2563eb", "label": "y = x^2 - 9"}],
            "dots": [[-3, 0, "#059669", "(-3, 0)"], [3, 0, "#059669", "(3, 0)"]],
        },
        "rule": r"x^2 = k \implies x = \pm\sqrt{k}",
        "segments": [
            {
                "narration": "When a quadratic has no b x term, solve it by isolating x squared!",
                "label": "Equation",
                "tex": r"2x^2 - 18 = 0",
                "color": "#0f172a",
            },
            {
                "narration": "Add 18 to both sides and divide by 2 to get x squared equals 9.",
                "label": "Isolate x²",
                "tex": r"2x^2 = 18 \implies x^2 = 9",
                "color": "#2563eb",
            },
            {
                "narration": "Take the square root of both sides—and don't forget plus or minus! The parabola crosses at both negative 3 and positive 3.",
                "label": "Two Symmetric Roots",
                "tex": r"x = \pm\sqrt{9} \implies x = 3, -3",
                "color": "#059669",
            },
            {
                "narration": "Try this vertex-form equation: solve x minus 1 squared minus 16 equals 0.",
                "label": "Try It Yourself",
                "tex": r"(x - 1)^2 - 16 = 0",
                "color": "#0f172a",
            },
            {
                "narration": "x minus 1 equals plus or minus 4, so adding 1 gives x equals 5 and x equals negative 3!",
                "label": "Solution",
                "tex": r"x = 5,\quad x = -3",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "solve_qe_quadratic_formula",
        "title": "Solve Using Quadratic Formula",
        "subtitle": "MPM2D • Works for Every Quadratic",
        "visual": "algebra",
        "rule": r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
        "segments": [
            {
                "narration": "When a quadratic won't factor with integers, the quadratic formula solves it every single time.",
                "label": "Standard Form",
                "tex": r"ax^2 + bx + c = 0",
                "color": "#2563eb",
            },
            {
                "narration": "Let's solve x squared plus 4 x plus 1 equals 0. Here a is 1, b is 4, and c is 1.",
                "label": "Identify a, b, c",
                "tex": r"a = 1,\quad b = 4,\quad c = 1",
                "color": "#0f172a",
            },
            {
                "narration": "Plug them into negative b plus or minus the square root of b squared minus 4 a c, all over 2 a.",
                "label": "Substitute",
                "tex": r"x = \frac{-4 \pm \sqrt{4^2 - 4(1)(1)}}{2(1)}",
                "color": "#059669",
            },
            {
                "narration": "16 minus 4 is 12, and root 12 simplifies to 2 root 3. Dividing by 2 gives negative 2 plus or minus root 3.",
                "label": "Exact Roots",
                "tex": r"x = -2 \pm \sqrt{3}",
                "color": "#d97706",
            },
            {
                "narration": "Try one yourself: solve 2 x squared minus 3 x minus 2 equals 0.",
                "label": "Try It Yourself",
                "tex": r"2x^2 - 3x - 2 = 0",
                "color": "#0f172a",
            },
            {
                "narration": "The discriminant is 9 plus 16 equals 25, whose square root is 5. That gives x equals 2 and x equals negative 0.5!",
                "label": "Solution",
                "tex": r"x = 2,\quad x = -\frac{1}{2}",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "transformations_quadratic",
        "title": "Transformations of Quadratics",
        "subtitle": "MPM2D • Parent Parabola y = x²",
        "visual": "graph",
        "graph": {
            "x_range": [-6, 6, 1],
            "y_range": [-8, 8, 2],
            "curves": [
                {"a": 1, "h": 0, "k": 0, "color": "#94a3b8", "label": "y = x^2"},
                {"a": -2, "h": 2, "k": 5, "color": "#2563eb", "label": "y = -2(x-2)^2 + 5"},
            ],
            "dots": [[0, 0, "#94a3b8", "(0,0)"], [2, 5, "#d97706", "V(2,5)"]],
        },
        "rule": r"y = a(x - h)^2 + k",
        "segments": [
            {
                "narration": "Look at the grey parent parabola y equals x squared. Every transformation in vertex form moves or stretches it!",
                "label": "Parent Function",
                "tex": r"y = x^2 \rightarrow y = a(x - h)^2 + k",
                "color": "#0f172a",
            },
            {
                "narration": "a controls vertical stretch and reflection. When a is negative 2, the blue parabola flips upside down and stretches twice as narrow.",
                "label": "a = -2 (Flip & Stretch)",
                "tex": r"a < 0 \implies \text{opens down}",
                "color": "#2563eb",
            },
            {
                "narration": "h shifts left or right—watch the opposite sign! x minus 2 shifts 2 units right, and plus 5 shifts 5 units up to the new vertex 2, 5.",
                "label": "h = 2, k = 5",
                "tex": r"\text{Right } 2,\; \text{Up } 5 \implies V(2, 5)",
                "color": "#059669",
            },
            {
                "narration": "Your turn: describe the transformations for y equals 0.5 times x plus 3 squared minus 4.",
                "label": "Try It Yourself",
                "tex": r"y = 0.5(x + 3)^2 - 4",
                "color": "#0f172a",
            },
            {
                "narration": "Vertical compression by 0.5, shift 3 units left, and shift 4 units down!",
                "label": "Solution",
                "tex": r"\text{Compress } 0.5,\; \text{Left } 3,\; \text{Down } 4",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "axis_symmetry_factored",
        "title": "Axis of Symmetry: Factored Form",
        "subtitle": "MPM2D • Midpoint of Zeros",
        "visual": "graph",
        "graph": {
            "x_range": [-2, 9, 1],
            "y_range": [-10, 6, 2],
            "curves": [{"a": 1, "h": 4, "k": -9, "color": "#2563eb", "label": "y = (x-1)(x-7)"}],
            "dots": [[1, 0, "#059669", "r=1"], [7, 0, "#059669", "s=7"], [4, -9, "#d97706", "x=4"]],
            "aos": 4,
        },
        "rule": r"y = a(x - r)(x - s) \implies x = \frac{r + s}{2}",
        "segments": [
            {
                "narration": "In factored form, the parabola crosses the x-axis at r and s. Because it's symmetric, the axis of symmetry is right in the middle!",
                "label": "Factored Form",
                "tex": r"y = (x - 1)(x - 7)",
                "color": "#0f172a",
            },
            {
                "narration": "Flip the signs to read the x-intercepts: r equals 1 and s equals 7, shown as green dots on the graph.",
                "label": "x-Intercepts",
                "tex": r"r = 1,\quad s = 7",
                "color": "#059669",
            },
            {
                "narration": "Average them: 1 plus 7 divided by 2 equals 4. That dashed red line at x equals 4 cuts the parabola in half!",
                "label": "Axis of Symmetry",
                "tex": r"x = \frac{1 + 7}{2} = 4",
                "color": "#d97706",
            },
            {
                "narration": "Try one: find the axis of symmetry for y equals negative 3 times x plus 5 times x minus 1.",
                "label": "Try It Yourself",
                "tex": r"y = -3(x + 5)(x - 1)",
                "color": "#0f172a",
            },
            {
                "narration": "The zeros are negative 5 and 1. Their average is negative 5 plus 1 over 2, which equals x equals negative 2!",
                "label": "Solution",
                "tex": r"x = \frac{-5 + 1}{2} = -2",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "axis_symmetry_vertex",
        "title": "Axis of Symmetry: Vertex Form",
        "subtitle": "MPM2D • Straight Through the Vertex",
        "visual": "graph",
        "graph": {
            "x_range": [-1, 8, 1],
            "y_range": [-2, 10, 2],
            "curves": [{"a": 1, "h": 4, "k": 2, "color": "#2563eb", "label": "y = (x-4)^2 + 2"}],
            "dots": [[4, 2, "#d97706", "V(4, 2)"]],
            "aos": 4,
        },
        "rule": r"y = a(x - h)^2 + k \implies x = h",
        "segments": [
            {
                "narration": "Finding the axis of symmetry from vertex form is the fastest of all—because the line passes straight through the vertex!",
                "label": "Vertex Form",
                "tex": r"y = (x - 4)^2 + 2",
                "color": "#0f172a",
            },
            {
                "narration": "Flip the sign inside the bracket: x minus 4 means h equals positive 4, so the vertex is 4, 2.",
                "label": "Vertex",
                "tex": r"V(4, 2)",
                "color": "#2563eb",
            },
            {
                "narration": "Therefore, the dashed axis of symmetry is simply x equals 4.",
                "label": "Axis of Symmetry",
                "tex": r"x = 4",
                "color": "#d97706",
            },
            {
                "narration": "Try this one: what is the axis of symmetry of y equals negative 0.5 times x plus 6 squared minus 9?",
                "label": "Try It Yourself",
                "tex": r"y = -0.5(x + 6)^2 - 9",
                "color": "#0f172a",
            },
            {
                "narration": "x plus 6 means h is negative 6, so the axis of symmetry is x equals negative 6!",
                "label": "Solution",
                "tex": r"x = -6",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "axis_symmetry_standard",
        "title": "Axis of Symmetry: Standard Form",
        "subtitle": "MPM2D • Use x = -b / 2a",
        "visual": "graph",
        "graph": {
            "x_range": [-2, 6, 1],
            "y_range": [-5, 9, 2],
            "curves": [{"a": 2, "h": 2, "k": -3, "color": "#2563eb", "label": "y = 2x^2 - 8x + 5"}],
            "dots": [[2, -3, "#d97706", "V(2, -3)"]],
            "aos": 2,
        },
        "rule": r"y = ax^2 + bx + c \implies x = -\frac{b}{2a}",
        "segments": [
            {
                "narration": "In standard form, you don't need to factor or complete the square just to find the axis of symmetry.",
                "label": "Standard Form",
                "tex": r"y = 2x^2 - 8x + 5",
                "color": "#0f172a",
            },
            {
                "narration": "Just use x equals negative b over 2 a! Here a is 2 and b is negative 8.",
                "label": "Substitute a, b",
                "tex": r"x = -\frac{-8}{2(2)} = \frac{8}{4}",
                "color": "#2563eb",
            },
            {
                "narration": "8 divided by 4 is 2, matching the dashed line through the vertex at x equals 2.",
                "label": "Axis of Symmetry",
                "tex": r"x = 2",
                "color": "#d97706",
            },
            {
                "narration": "Try one: find the axis of symmetry for y equals negative 3 x squared minus 12 x plus 7.",
                "label": "Try It Yourself",
                "tex": r"y = -3x^2 - 12x + 7",
                "color": "#0f172a",
            },
            {
                "narration": "Negative of negative 12 is 12, divided by 2 times negative 3 which is negative 6, giving x equals negative 2!",
                "label": "Solution",
                "tex": r"x = -2",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "expand_distributive",
        "title": "Expand by Distributive Property",
        "subtitle": "MPM2D • Factored to Standard Form",
        "visual": "algebra",
        "rule": r"(a + b)(c + d) = a(c + d) + b(c + d)",
        "segments": [
            {
                "narration": "Expanding converts factored form into standard form using the distributive property.",
                "label": "Factored Form",
                "tex": r"(x + 3)(x + 5)",
                "color": "#0f172a",
            },
            {
                "narration": "Multiply each term in the first bracket by the entire second bracket: x times x plus 5, plus 3 times x plus 5.",
                "label": "Distribute",
                "tex": r"x(x + 5) + 3(x + 5)",
                "color": "#2563eb",
            },
            {
                "narration": "Multiply out each part to get x squared plus 5 x plus 3 x plus 15, then combine the like terms in the middle.",
                "label": "Standard Form",
                "tex": r"x^2 + 8x + 15",
                "color": "#059669",
            },
            {
                "narration": "Try one yourself: expand 2 x minus 1 times x plus 4.",
                "label": "Try It Yourself",
                "tex": r"(2x - 1)(x + 4)",
                "color": "#0f172a",
            },
            {
                "narration": "2 x squared plus 8 x minus x minus 4 simplifies to 2 x squared plus 7 x minus 4!",
                "label": "Solution",
                "tex": r"2x^2 + 7x - 4",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "expand_area_model",
        "title": "Expand Using an Area Model",
        "subtitle": "MPM2D • Visual Box Multiplication",
        "visual": "area",
        "area_labels": ["x", "+2", "x", "+4", "x^2", "4x", "2x", "8"],
        "rule": r"\text{Total Area} = \sum \text{Region Areas}",
        "segments": [
            {
                "narration": "An area model turns binomial multiplication into four simple rectangle areas!",
                "label": "Dimensions",
                "tex": r"(x + 2)(x + 4)",
                "color": "#0f172a",
            },
            {
                "narration": "Put x and plus 2 along the top, and x and plus 4 along the side. Multiply each box: x squared, 4 x, 2 x, and 8.",
                "label": "4 Area Regions",
                "tex": r"x^2 + 4x + 2x + 8",
                "color": "#2563eb",
            },
            {
                "narration": "Combine the two x terms 4 x plus 2 x to get x squared plus 6 x plus 8.",
                "label": "Standard Form",
                "tex": r"x^2 + 6x + 8",
                "color": "#059669",
            },
            {
                "narration": "Try one yourself using the box method: expand x plus 5 times x minus 3.",
                "label": "Try It Yourself",
                "tex": r"(x + 5)(x - 3)",
                "color": "#0f172a",
            },
            {
                "narration": "The four boxes are x squared, 5 x, negative 3 x, and negative 15, giving x squared plus 2 x minus 15!",
                "label": "Solution",
                "tex": r"x^2 + 2x - 15",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "expand_special_product",
        "title": "Expand Special Products",
        "subtitle": "MPM2D • Avoid the (x+3)² Trap!",
        "visual": "area",
        "area_labels": ["x", "+3", "x", "+3", "x^2", "3x", "3x", "9"],
        "rule": r"(a + b)^2 = a^2 + 2ab + b^2",
        "segments": [
            {
                "narration": "Watch out for the number-one algebra trap: x plus 3 all squared is NOT x squared plus 9!",
                "label": "Common Trap",
                "tex": r"(x + 3)^2 \neq x^2 + 9",
                "color": "#dc2626",
            },
            {
                "narration": "Look at the area model for x plus 3 times x plus 3: besides x squared and 9, there are TWO 3 x rectangles!",
                "label": "Two Middle Terms",
                "tex": r"x^2 + 3x + 3x + 9",
                "color": "#2563eb",
            },
            {
                "narration": "So x plus 3 squared equals x squared plus 6 x plus 9.",
                "label": "Expanded Form",
                "tex": r"x^2 + 6x + 9",
                "color": "#059669",
            },
            {
                "narration": "Try one yourself: expand 2 x minus 5 all squared.",
                "label": "Try It Yourself",
                "tex": r"(2x - 5)^2",
                "color": "#0f172a",
            },
            {
                "narration": "Square 2 x to get 4 x squared, double the product to get minus 20 x, and square minus 5 to get plus 25!",
                "label": "Solution",
                "tex": r"4x^2 - 20x + 25",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "discriminant_x_intercepts",
        "title": "Discriminant & x-Intercepts",
        "subtitle": "MPM2D • How Many Zeros?",
        "visual": "graph",
        "graph": {
            "x_range": [-3, 3, 1],
            "y_range": [-3, 6, 1],
            "curves": [
                {"a": 1, "h": 0, "k": -2, "color": "#059669", "label": "D > 0 (2 roots)"},
                {"a": 1, "h": 0, "k": 0, "color": "#2563eb", "label": "D = 0 (1 root)"},
                {"a": 1, "h": 0, "k": 2, "color": "#dc2626", "label": "D < 0 (0 roots)"},
            ],
            "dots": [[-1.41, 0, "#059669", ""], [1.41, 0, "#059669", ""], [0, 0, "#2563eb", ""]],
        },
        "rule": r"D = b^2 - 4ac",
        "segments": [
            {
                "narration": "How many times does a parabola cross the x-axis? Check the discriminant: b squared minus 4 a c!",
                "label": "Discriminant",
                "tex": r"D = b^2 - 4ac",
                "color": "#0f172a",
            },
            {
                "narration": "If D is positive, like the green parabola, there are 2 x-intercepts. If D is 0, like the blue parabola, the vertex touches once. If D is negative, like the red curve, there are 0 real x-intercepts!",
                "label": "Three Cases",
                "tex": r"D > 0 \;(2),\quad D = 0 \;(1),\quad D < 0 \;(0)",
                "color": "#2563eb",
            },
            {
                "narration": "Let's test one: how many x-intercepts does y equals 2 x squared minus 4 x plus 5 have?",
                "label": "Try It Yourself",
                "tex": r"y = 2x^2 - 4x + 5",
                "color": "#0f172a",
            },
            {
                "narration": "D equals negative 4 squared minus 4 times 2 times 5, which is 16 minus 40 equals negative 24. Since D is negative, there are 0 x-intercepts!",
                "label": "Solution",
                "tex": r"D = -24 < 0 \implies 0\text{ x-intercepts}",
                "color": "#dc2626",
            },
        ],
    },
    {
        "id": "completing_the_square",
        "title": "Completing the Square",
        "subtitle": "MPM2D • Standard to Vertex Form",
        "visual": "area",
        "area_labels": ["x", "+3", "x", "+3", "x^2", "3x", "3x", "9"],
        "rule": r"x^2 + bx = \left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2",
        "segments": [
            {
                "narration": "To convert y equals x squared plus 6 x plus 5 to vertex form, we literally complete a geometric square!",
                "label": "Standard Form",
                "tex": r"y = x^2 + 6x + 5",
                "color": "#0f172a",
            },
            {
                "narration": "Split 6 x into two 3 x strips around the x squared box. Look at the missing corner: 3 times 3 equals 9!",
                "label": "Half of 6, Squared = 9",
                "tex": r"y = (x^2 + 6x + 9 - 9) + 5",
                "color": "#2563eb",
            },
            {
                "narration": "The completed square factors into x plus 3 squared, and negative 9 plus 5 simplifies to minus 4.",
                "label": "Vertex Form",
                "tex": r"y = (x + 3)^2 - 4",
                "color": "#059669",
            },
            {
                "narration": "Try one yourself: complete the square for y equals x squared minus 8 x plus 10.",
                "label": "Try It Yourself",
                "tex": r"y = x^2 - 8x + 10",
                "color": "#0f172a",
            },
            {
                "narration": "Half of negative 8 is negative 4, squared is 16. Add and subtract 16 to get x minus 4 squared minus 6!",
                "label": "Solution",
                "tex": r"y = (x - 4)^2 - 6",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "vertex_optimal_value",
        "title": "Vertex & Max/Min Optimal Value",
        "subtitle": "MPM2D • Opens Up vs Opens Down",
        "visual": "graph",
        "graph": {
            "x_range": [-1, 7, 1],
            "y_range": [-2, 10, 2],
            "curves": [{"a": -1, "h": 3, "k": 8, "color": "#2563eb", "label": "y = -(x-3)^2 + 8"}],
            "dots": [[3, 8, "#d97706", "Max V(3, 8)"]],
        },
        "rule": r"a > 0 \implies \text{Min } k \quad | \quad a < 0 \implies \text{Max } k",
        "segments": [
            {
                "narration": "In vertex form, the vertex h, k gives us the highest or lowest point on the parabola—called the optimal value!",
                "label": "Vertex Form",
                "tex": r"y = -2(x - 3)^2 + 8",
                "color": "#0f172a",
            },
            {
                "narration": "Here the vertex is 3, 8. Because a is negative, the parabola opens downward like a hill.",
                "label": "Opens Down (a < 0)",
                "tex": r"V(3, 8) \implies \text{Maximum}",
                "color": "#2563eb",
            },
            {
                "narration": "So the maximum optimal value is y equals 8, and it occurs when x equals 3.",
                "label": "Optimal Value",
                "tex": r"\text{Max } y = 8 \text{ at } x = 3",
                "color": "#059669",
            },
            {
                "narration": "Try one: find the optimal value of y equals 4 times x plus 1 squared minus 7.",
                "label": "Try It Yourself",
                "tex": r"y = 4(x + 1)^2 - 7",
                "color": "#0f172a",
            },
            {
                "narration": "Since a equals 4 is positive, it opens upward, giving a minimum value of negative 7 at x equals negative 1!",
                "label": "Solution",
                "tex": r"\text{Min } y = -7 \text{ at } x = -1",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "equation_from_graph_vertex",
        "title": "Equation from Vertex & Point",
        "subtitle": "MPM2D • Solving for a",
        "visual": "graph",
        "graph": {
            "x_range": [-2, 6, 1],
            "y_range": [-5, 7, 2],
            "curves": [{"a": 2, "h": 2, "k": -3, "color": "#2563eb", "label": "y = 2(x-2)^2 - 3"}],
            "dots": [[2, -3, "#d97706", "V(2,-3)"], [4, 5, "#059669", "P(4,5)"]],
        },
        "rule": r"\text{Sub } (h, k) \text{ and } (x, y) \text{ to solve for } a",
        "segments": [
            {
                "narration": "If a graph gives you the vertex 2, negative 3 and another point 4, 5, always start with vertex form!",
                "label": "Plug in Vertex (2, -3)",
                "tex": r"y = a(x - 2)^2 - 3",
                "color": "#0f172a",
            },
            {
                "narration": "Next, substitute the green point x equals 4 and y equals 5 into the equation.",
                "label": "Sub Point (4, 5)",
                "tex": r"5 = a(4 - 2)^2 - 3",
                "color": "#2563eb",
            },
            {
                "narration": "4 minus 2 is 2, squared is 4. Add 3 to get 8 equals 4 a, so a equals 2!",
                "label": "Solve for a",
                "tex": r"8 = 4a \implies a = 2 \implies y = 2(x - 2)^2 - 3",
                "color": "#059669",
            },
            {
                "narration": "Try one yourself: vertex 1, 4 passing through 3, negative 4.",
                "label": "Try It Yourself",
                "tex": r"V(1, 4),\; P(3, -4)",
                "color": "#0f172a",
            },
            {
                "narration": "Negative 4 equals a times 3 minus 1 squared plus 4 gives negative 8 equals 4 a, so a equals negative 2!",
                "label": "Solution",
                "tex": r"y = -2(x - 1)^2 + 4",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "graphing_step_pattern",
        "title": "Graphing with the Step Pattern",
        "subtitle": "MPM2D • Fast Parabola Sketching",
        "visual": "graph",
        "graph": {
            "x_range": [-2, 5, 1],
            "y_range": [-4, 8, 2],
            "curves": [{"a": 2, "h": 1, "k": -3, "color": "#2563eb", "label": "y = 2(x-1)^2 - 3"}],
            "dots": [[1, -3, "#d97706", "V(1,-3)"], [2, -1, "#059669", "+2"], [3, 5, "#059669", "+6"]],
        },
        "rule": r"\text{Step Pattern} = a \times (1, 3, 5, \dots)",
        "segments": [
            {
                "narration": "Want to graph a parabola in 10 seconds without a table of values? Use the step pattern!",
                "label": "Vertex Form",
                "tex": r"y = 2(x - 1)^2 - 3",
                "color": "#0f172a",
            },
            {
                "narration": "Plot the vertex at 1, negative 3. Then multiply the basic 1, 3, 5 pattern by a equals 2 to get 2, 6, 10.",
                "label": "Multiply by a = 2",
                "tex": r"2 \times (1, 3, 5) = (2, 6, 10)",
                "color": "#2563eb",
            },
            {
                "narration": "Step right 1, up 2 to hit 2, negative 1. Step right 1, up 6 to hit 3, 5, and mirror to the left!",
                "label": "Plot & Mirror",
                "tex": r"(1, -3) \rightarrow (2, -1) \rightarrow (3, 5)",
                "color": "#059669",
            },
            {
                "narration": "Try one: what is the step pattern for y equals negative 0.5 times x plus 2 squared plus 6?",
                "label": "Try It Yourself",
                "tex": r"y = -0.5(x + 2)^2 + 6",
                "color": "#0f172a",
            },
            {
                "narration": "Multiply 1, 3, 5 by negative 0.5 to step down by 0.5, 1.5, and 2.5!",
                "label": "Solution",
                "tex": r"(-0.5,\; -1.5,\; -2.5)",
                "color": "#d97706",
            },
        ],
    },
    {
        "id": "quadratic_word_problem_max_area",
        "title": "Max Area Optimization Problem",
        "subtitle": "MPM2D • Quadratic Word Problem",
        "visual": "graph",
        "graph": {
            "x_range": [-2, 22, 5],
            "y_range": [-20, 240, 50],
            "curves": [{"a": -2, "h": 10, "k": 200, "color": "#2563eb", "label": "A(w) = w(40-2w)"}],
            "dots": [[0, 0, "#059669", "0"], [20, 0, "#059669", "20"], [10, 200, "#d97706", "Max(10, 200)"]],
            "aos": 10,
        },
        "rule": r"\text{Optimal } x = \frac{r + s}{2} \implies \text{Max Area}",
        "segments": [
            {
                "narration": "A farmer has 40 meters of fencing for 3 sides of a pen. 2 w plus l equals 40, so l equals 40 minus 2 w.",
                "label": "Area Function",
                "tex": r"A(w) = w(40 - 2w)",
                "color": "#0f172a",
            },
            {
                "narration": "Look at the parabola: its zeros are w equals 0 and w equals 20.",
                "label": "Find Zeros",
                "tex": r"w = 0 \quad \text{and} \quad w = 20",
                "color": "#2563eb",
            },
            {
                "narration": "The maximum area sits right at the vertex halfway between them: w equals 10 meters, giving 200 square meters!",
                "label": "Max Area at Vertex",
                "tex": r"w = 10\text{ m} \implies A(10) = 200\text{ m}^2",
                "color": "#059669",
            },
            {
                "narration": "Try one yourself: what is the maximum area with 60 meters of fencing on 3 sides?",
                "label": "Try It Yourself",
                "tex": r"A(w) = w(60 - 2w)",
                "color": "#0f172a",
            },
            {
                "narration": "Zeros are 0 and 30, so optimal width is 15 meters, giving 15 times 30 equals 450 square meters!",
                "label": "Solution",
                "tex": r"w = 15\text{ m} \implies A_{\max} = 450\text{ m}^2",
                "color": "#d97706",
            },
        ],
    },
]


def pick_topic(topic_id: Optional[str] = None, offset: int = 0) -> Dict[str, Any]:
    """Return a specific topic by ID, or rotate automatically based on UTC date + offset."""
    if topic_id:
        for t in TOPICS:
            if t["id"] == topic_id:
                return t
        raise ValueError(f"Unknown topic_id: {topic_id}")

    now = datetime.now(timezone.utc)
    day_index = int(now.timestamp() // 86400)
    idx = (day_index * 4 + offset) % len(TOPICS)
    return TOPICS[idx]
