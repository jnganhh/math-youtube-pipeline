"""
mpm2d_topics.py
Curriculum-aligned MPM2D (Ontario Grade 10 Academic Math) Quadratic Topics.
Each topic includes a ~2:30 (150s) structured lesson:
1. Hook & Core Idea
2. Worked Example (step-by-step)
3. Practice Problem ("Try It Yourself") + Solution
4. Key Takeaway
"""

from datetime import datetime, timezone
from typing import Dict, List, Optional, Any

TOPICS: List[Dict[str, Any]] = [
    {
        "id": "factoring_common_factor",
        "title": "Factoring by Common Factor",
        "rule": r"\text{GCF}(a, b) \cdot \left(\frac{a}{\text{GCF}} + \frac{b}{\text{GCF}}\right)",
        "voiceover": (
            "Welcome to Grade 10 Academic Math, M P M 2 D! Today we are mastering factoring by common factor. "
            "Whenever you factor any quadratic or polynomial expression, your very first step should always be checking for a greatest common factor, or G C F. "
            "Let's look at our first worked example: 6 x squared plus 9 x. "
            "First, look at the coefficients 6 and 9. The largest number that divides evenly into both 6 and 9 is 3. "
            "Next, look at the variable parts: x squared and x. Both terms contain at least one x, so the variable part of our G C F is x. "
            "Putting them together, our greatest common factor is 3 x. "
            "Now, write 3 x in front of a set of brackets, and divide each original term by 3 x. "
            "6 x squared divided by 3 x gives 2 x. And 9 x divided by 3 x gives 3. "
            "So our factored expression is 3 x times 2 x plus 3. You can always check your answer by expanding: 3 x times 2 x is 6 x squared, and 3 x times 3 is 9 x! "
            "Now, let's try a practice problem together. Pause and think about how to factor 10 x squared minus 15 x. "
            "First, find the greatest common factor of 10 and 15, which is 5. Both terms also share an x, so the G C F is 5 x. "
            "Divide each term by 5 x: 10 x squared divided by 5 x is 2 x, and negative 15 x divided by 5 x is negative 3. "
            "So the final factored form is 5 x times 2 x minus 3. "
            "Remember: always pull out the G C F first—it makes every other factoring method much easier!"
        ),
        "steps": [
            ("Example 1", r"6x^2 + 9x", "#0f172a"),
            ("Find GCF", r"\text{GCF}(6x^2, 9x) = 3x", "#2563eb"),
            ("Divide Each Term", r"3x\left(\frac{6x^2}{3x} + \frac{9x}{3x}\right)", "#059669"),
            ("Factored Form", r"3x(2x + 3)", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"10x^2 - 15x", "#0f172a"),
            ("GCF = 5x", r"5x\left(\frac{10x^2}{5x} - \frac{15x}{5x}\right)", "#2563eb"),
            ("Answer", r"5x(2x - 3)", "#059669"),
        ],
    },
    {
        "id": "factoring_grouping",
        "title": "Factoring by Grouping",
        "rule": r"a(x + y) + b(x + y) = (x + y)(a + b)",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are learning how to factor by grouping. "
            "You use factoring by grouping whenever an expression has four terms and no single common factor across all four. "
            "Let's work through an example: x cubed plus 3 x squared plus 2 x plus 6. "
            "Step one: group the first two terms together, and group the last two terms together. "
            "Step two: factor out the greatest common factor from each pair separately. "
            "From x cubed plus 3 x squared, we can factor out x squared, leaving x plus 3 inside the brackets. "
            "From 2 x plus 6, we can factor out positive 2, also leaving x plus 3 inside the brackets. "
            "Notice that both groups now share the exact same binomial factor: x plus 3! "
            "Step three: factor out that common binomial x plus 3, and put the remaining pieces x squared plus 2 into the second bracket. "
            "So our final answer is x plus 3 times x squared plus 2. "
            "Now let's try a practice problem: factor x cubed minus 4 x squared plus 5 x minus 20. "
            "Group the first two terms and factor out x squared to get x squared times x minus 4. "
            "Group the last two terms and factor out positive 5 to get 5 times x minus 4. "
            "Factor out the common binomial x minus 4, giving x minus 4 times x squared plus 5. "
            "Whenever you see four terms, pair them up and look for that matching bracket!"
        ),
        "steps": [
            ("Example 1", r"x^3 + 3x^2 + 2x + 6", "#0f172a"),
            ("Group in Pairs", r"(x^3 + 3x^2) + (2x + 6)", "#2563eb"),
            ("Factor Each Pair", r"x^2(x + 3) + 2(x + 3)", "#059669"),
            ("Factored Form", r"(x + 3)(x^2 + 2)", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"x^3 - 4x^2 + 5x - 20", "#0f172a"),
            ("Factor Pairs", r"x^2(x - 4) + 5(x - 4)", "#2563eb"),
            ("Answer", r"(x - 4)(x^2 + 5)", "#059669"),
        ],
    },
    {
        "id": "factoring_sum_product",
        "title": "Factoring Simple Trinomials",
        "rule": r"x^2 + (p+q)x + pq = (x + p)(x + q)",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are factoring simple trinomials using the sum and product method. "
            "A simple trinomial has the form x squared plus b x plus c, where the coefficient in front of x squared is 1. "
            "Let's factor x squared plus 7 x plus 12. "
            "To factor this, we need two integers that multiply to give c, which is 12, and add to give b, which is 7. "
            "Let's list factor pairs of 12: 1 times 12 adds to 13. 2 times 6 adds to 8. 3 times 4 is 12, and 3 plus 4 equals 7! "
            "That's our pair: 3 and 4. "
            "Because the leading coefficient is 1, we can write the factored form directly as x plus 3 times x plus 4. "
            "Always do a quick mental check: x times x is x squared, 3 x plus 4 x is 7 x, and 3 times 4 is 12. "
            "Now let's try a practice problem with negatives: factor x squared minus 2 x minus 15. "
            "We need two numbers that multiply to negative 15 and add to negative 2. "
            "Since the product is negative, one number is positive and one is negative. "
            "Negative 5 times 3 is negative 15, and negative 5 plus 3 is negative 2. "
            "So the factored form is x minus 5 times x plus 3. "
            "Master sum and product—it's the foundation for solving quadratics!"
        ),
        "steps": [
            ("Example 1", r"x^2 + 7x + 12", "#0f172a"),
            ("Product = 12, Sum = 7", r"3 \times 4 = 12,\quad 3 + 4 = 7", "#2563eb"),
            ("Factored Form", r"(x + 3)(x + 4)", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"x^2 - 2x - 15", "#0f172a"),
            ("Product = -15, Sum = -2", r"(-5)(3) = -15,\; -5 + 3 = -2", "#2563eb"),
            ("Answer", r"(x - 5)(x + 3)", "#059669"),
        ],
    },
    {
        "id": "factoring_decomposition",
        "title": "Factoring by Decomposition",
        "rule": r"ax^2 + bx + c \rightarrow \text{split } bx \text{ using } ac",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are tackling complex trinomials using factoring by decomposition. "
            "Use decomposition when the coefficient a in front of x squared is not 1 and cannot be factored out as a G C F. "
            "Let's factor 2 x squared plus 7 x plus 3. "
            "Step one: multiply a times c. Here, 2 times 3 equals 6. "
            "Step two: find two numbers that multiply to 6 and add to b, which is 7. Those numbers are 6 and 1. "
            "Step three: decompose the middle term 7 x into 6 x plus 1 x. Now we have four terms: 2 x squared plus 6 x plus 1 x plus 3. "
            "Step four: factor by grouping! Factor 2 x from the first pair to get 2 x times x plus 3, and factor 1 from the second pair to get 1 times x plus 3. "
            "Factor out the common bracket x plus 3, giving 2 x plus 1 times x plus 3. "
            "Now let's try a practice problem: factor 3 x squared plus 10 x plus 8. "
            "Multiply a times c: 3 times 8 is 24. Two numbers that multiply to 24 and add to 10 are 6 and 4. "
            "Split 10 x into 6 x plus 4 x, group into 3 x times x plus 2 plus 4 times x plus 2, and we get 3 x plus 4 times x plus 2!"
        ),
        "steps": [
            ("Example 1", r"2x^2 + 7x + 3", "#0f172a"),
            ("ac = 6, Sum = 7", r"6 \times 1 = 6,\quad 6 + 1 = 7", "#2563eb"),
            ("Decompose bx", r"2x^2 + 6x + 1x + 3", "#059669"),
            ("Group & Factor", r"(2x + 1)(x + 3)", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"3x^2 + 10x + 8", "#0f172a"),
            ("ac = 24, Split 6x + 4x", r"3x(x + 2) + 4(x + 2)", "#2563eb"),
            ("Answer", r"(3x + 4)(x + 2)", "#059669"),
        ],
    },
    {
        "id": "factoring_special_product",
        "title": "Factoring Special Products",
        "rule": r"a^2 - b^2 = (a + b)(a - b)",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are factoring special products, focusing on difference of squares and perfect square trinomials. "
            "First, a difference of squares has two perfect square terms separated by a minus sign: a squared minus b squared. "
            "It always factors into a plus b times a minus b. "
            "Let's factor 9 x squared minus 16. "
            "Notice that 9 x squared is 3 x all squared, and 16 is 4 squared. "
            "Using the pattern, a is 3 x and b is 4, so it factors immediately into 3 x plus 4 times 3 x minus 4. "
            "Notice there is no middle x term because positive 12 x and negative 12 x cancel out! "
            "Be careful: a sum of squares like x squared plus 16 cannot be factored over the real numbers. "
            "Now let's try a practice problem: factor 25 x squared minus 49. "
            "25 x squared is 5 x all squared, and 49 is 7 squared. "
            "Apply the difference of squares rule: 5 x plus 7 times 5 x minus 7. "
            "Always scan for perfect squares—it saves huge amounts of time on tests!"
        ),
        "steps": [
            ("Example 1", r"9x^2 - 16", "#0f172a"),
            ("Rewrite as Squares", r"(3x)^2 - (4)^2", "#2563eb"),
            ("Factored Form", r"(3x + 4)(3x - 4)", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"25x^2 - 49", "#0f172a"),
            ("Identify a = 5x, b = 7", r"(5x)^2 - (7)^2", "#2563eb"),
            ("Answer", r"(5x + 7)(5x - 7)", "#059669"),
        ],
    },
    {
        "id": "solve_qe_factoring",
        "title": "Solve Quadratics by Factoring",
        "rule": r"AB = 0 \implies A = 0 \text{ or } B = 0",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are solving quadratic equations by factoring. "
            "The key idea is the Zero Product Property: if two factors multiply to zero, at least one of them must be zero. "
            "Let's solve x squared minus 5 x plus 6 equals 0. "
            "Step one: make sure the equation is set equal to zero. Here it already is. "
            "Step two: factor the left side using sum and product. We need two numbers that multiply to 6 and add to negative 5: negative 2 and negative 3. "
            "So we have x minus 2 times x minus 3 equals 0. "
            "Step three: set each factor equal to zero and solve. x minus 2 equals 0 gives x equals 2. x minus 3 equals 0 gives x equals 3. "
            "These two solutions, 2 and 3, are also the x-intercepts of the parabola! "
            "Now let's try a practice problem: solve x squared plus 3 x minus 10 equals 0. "
            "Factor using sum and product: 5 times negative 2 is negative 10, and 5 plus negative 2 is 3. "
            "So x plus 5 times x minus 2 equals 0. "
            "Setting each bracket to zero gives x equals negative 5 and x equals 2!"
        ),
        "steps": [
            ("Example 1", r"x^2 - 5x + 6 = 0", "#0f172a"),
            ("Factor", r"(x - 2)(x - 3) = 0", "#2563eb"),
            ("Zero Product Property", r"x - 2 = 0 \;\text{ or }\; x - 3 = 0", "#059669"),
            ("Solutions", r"x = 2,\quad x = 3", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"x^2 + 3x - 10 = 0", "#0f172a"),
            ("Factor", r"(x + 5)(x - 2) = 0", "#2563eb"),
            ("Answer", r"x = -5,\quad x = 2", "#059669"),
        ],
    },
    {
        "id": "solve_qe_isolation",
        "title": "Solve Quadratics by Isolation",
        "rule": r"x^2 = k \implies x = \pm\sqrt{k}",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are solving quadratic equations by isolation. "
            "When a quadratic equation has no b x term, or is already in vertex form, isolating the squared term is the fastest way to solve it. "
            "Let's solve 2 x squared minus 18 equals 0. "
            "Step one: add 18 to both sides to get 2 x squared equals 18. "
            "Step two: divide both sides by 2 to isolate x squared, giving x squared equals 9. "
            "Step three: take the square root of both sides. Remember the most common mistake students make: forgetting the plus or minus sign! "
            "Both 3 squared and negative 3 squared equal 9, so x equals plus or minus 3. "
            "Now let's try a practice problem in vertex form: solve x minus 1 all squared minus 16 equals 0. "
            "Add 16 to both sides: x minus 1 squared equals 16. "
            "Take the square root: x minus 1 equals plus or minus 4. "
            "Add 1 to both sides: x equals 1 plus 4, which is 5, or 1 minus 4, which is negative 3!"
        ),
        "steps": [
            ("Example 1", r"2x^2 - 18 = 0", "#0f172a"),
            ("Isolate x^2", r"2x^2 = 18 \implies x^2 = 9", "#2563eb"),
            ("Square Root", r"x = \pm\sqrt{9}", "#059669"),
            ("Solutions", r"x = 3,\quad x = -3", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"(x - 1)^2 - 16 = 0", "#0f172a"),
            ("Take Square Root", r"x - 1 = \pm 4", "#2563eb"),
            ("Answer", r"x = 5,\quad x = -3", "#059669"),
        ],
    },
    {
        "id": "solve_qe_quadratic_formula",
        "title": "Solve Using Quadratic Formula",
        "rule": r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are using the quadratic formula, the universal tool that solves every quadratic equation—even when it cannot be factored. "
            "For any equation in standard form a x squared plus b x plus c equals 0, the solutions are x equals negative b plus or minus the square root of b squared minus 4 a c, all divided by 2 a. "
            "Let's solve x squared plus 4 x plus 1 equals 0. "
            "Here, a equals 1, b equals 4, and c equals 1. "
            "Substitute carefully into the formula: x equals negative 4 plus or minus the square root of 4 squared minus 4 times 1 times 1, all over 2 times 1. "
            "Inside the square root, 16 minus 4 is 12. "
            "Since root 12 simplifies to 2 root 3, dividing both terms in the numerator by 2 gives x equals negative 2 plus or minus root 3. "
            "Now let's try a practice problem: solve 2 x squared minus 3 x minus 2 equals 0. "
            "With a equals 2, b equals negative 3, and c equals negative 2, the formula gives 3 plus or minus the square root of 9 plus 16, all over 4. "
            "Root 25 is 5, so x equals 3 plus 5 over 4, which is 2, or 3 minus 5 over 4, which is negative 0.5!"
        ),
        "steps": [
            ("Example 1", r"x^2 + 4x + 1 = 0", "#0f172a"),
            ("Quadratic Formula", r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", "#2563eb"),
            ("Substitute", r"x = \frac{-4 \pm \sqrt{16 - 4}}{2}", "#059669"),
            ("Exact Roots", r"x = -2 \pm \sqrt{3}", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"2x^2 - 3x - 2 = 0", "#0f172a"),
            ("Discriminant = 25", r"x = \frac{3 \pm \sqrt{25}}{4}", "#2563eb"),
            ("Answer", r"x = 2,\quad x = -\frac{1}{2}", "#059669"),
        ],
    },
    {
        "id": "transformations_quadratic",
        "title": "Transformations of Quadratics",
        "rule": r"y = a(x - h)^2 + k",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are describing transformations of quadratic functions from the parent parabola y equals x squared. "
            "In vertex form y equals a times x minus h squared plus k, each parameter controls a specific geometric transformation. "
            "First, a controls vertical stretch, compression, and reflection. If a is negative, the parabola reflects across the x-axis and opens downward. "
            "If the absolute value of a is greater than 1, it stretches vertically; if it's between 0 and 1, it compresses vertically. "
            "Second, h controls the horizontal translation. Because of the minus sign in x minus h, it shifts right when h is positive and left when h is negative—always watch the opposite sign! "
            "Third, k controls the vertical translation: up if k is positive, down if k is negative. "
            "Let's practice with y equals negative 2 times x plus 3 squared minus 5. "
            "Negative 2 means a reflection in the x-axis and a vertical stretch by a factor of 2. "
            "x plus 3 means a shift 3 units left, and minus 5 means a shift 5 units down!"
        ),
        "steps": [
            ("Vertex Form", r"y = a(x - h)^2 + k", "#0f172a"),
            ("a: Reflection / Stretch", r"a < 0 \implies \text{opens down}", "#2563eb"),
            ("h: Horizontal Shift", r"(x - h) \implies \text{right } h", "#059669"),
            ("k: Vertical Shift", r"+ k \implies \text{up } k", "#d97706"),
        ],
        "practice": [
            ("Describe", r"y = -2(x + 3)^2 - 5", "#0f172a"),
            ("a = -2, h = -3, k = -5", r"\text{Reflect, stretch 2}", "#2563eb"),
            ("Translations", r"\text{Left 3, Down 5}", "#059669"),
        ],
    },
    {
        "id": "axis_symmetry_factored",
        "title": "Axis of Symmetry: Factored Form",
        "rule": r"y = a(x - r)(x - s) \implies x = \frac{r + s}{2}",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are finding the axis of symmetry of a quadratic in factored form. "
            "Factored form is y equals a times x minus r times x minus s, where r and s are the x-intercepts, or zeros, of the parabola. "
            "Because every parabola is perfectly symmetric, its axis of symmetry must lie exactly halfway between its two x-intercepts! "
            "That means we just take the average of r and s: x equals r plus s divided by 2. "
            "Let's try an example: y equals 2 times x minus 1 times x minus 7. "
            "First, read off the x-intercepts by flipping the signs: r equals 1 and s equals 7. "
            "Now find their midpoint: 1 plus 7 divided by 2 equals 8 over 2, which is 4. "
            "So the axis of symmetry is x equals 4. "
            "Let's do a practice problem: y equals negative 3 times x plus 5 times x minus 1. "
            "The x-intercepts are negative 5 and positive 1. "
            "Average them: negative 5 plus 1 is negative 4, divided by 2 is negative 2. "
            "So the axis of symmetry is x equals negative 2!"
        ),
        "steps": [
            ("Factored Form", r"y = 2(x - 1)(x - 7)", "#0f172a"),
            ("x-Intercepts", r"r = 1,\quad s = 7", "#2563eb"),
            ("Midpoint Formula", r"x = \frac{1 + 7}{2}", "#059669"),
            ("Axis of Symmetry", r"x = 4", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"y = -3(x + 5)(x - 1)", "#0f172a"),
            ("Zeros: -5 and 1", r"x = \frac{-5 + 1}{2}", "#2563eb"),
            ("Answer", r"x = -2", "#059669"),
        ],
    },
    {
        "id": "axis_symmetry_vertex",
        "title": "Axis of Symmetry: Vertex Form",
        "rule": r"y = a(x - h)^2 + k \implies x = h",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are finding the axis of symmetry from vertex form. "
            "Vertex form is y equals a times x minus h squared plus k, where the vertex of the parabola is the point h, k. "
            "Since the axis of symmetry is the vertical line that cuts the parabola in half right through its vertex, "
            "its equation is simply x equals h! "
            "Let's look at an example: y equals 3 times x minus 4 squared plus 2. "
            "Remember to flip the sign inside the bracket: x minus 4 means h equals positive 4. "
            "So the vertex is 4, 2, and the axis of symmetry is x equals 4. "
            "Now let's try a practice problem: y equals negative 0.5 times x plus 6 squared minus 9. "
            "Inside the bracket we have x plus 6, which is x minus negative 6, so h equals negative 6. "
            "The vertex is negative 6, negative 9, and the axis of symmetry is x equals negative 6. "
            "Always remember to write x equals as an equation, not just a single number!"
        ),
        "steps": [
            ("Vertex Form", r"y = 3(x - 4)^2 + 2", "#0f172a"),
            ("Identify Vertex", r"V(4, 2)", "#2563eb"),
            ("Axis of Symmetry", r"x = 4", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"y = -0.5(x + 6)^2 - 9", "#0f172a"),
            ("Vertex: (-6, -9)", r"h = -6", "#2563eb"),
            ("Answer", r"x = -6", "#059669"),
        ],
    },
    {
        "id": "axis_symmetry_standard",
        "title": "Axis of Symmetry: Standard Form",
        "rule": r"y = ax^2 + bx + c \implies x = -\frac{b}{2a}",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are finding the axis of symmetry directly from standard form. "
            "Standard form is y equals a x squared plus b x plus c. "
            "You don't need to complete the square or factor just to find the axis of symmetry—you can use the formula x equals negative b over 2 a! "
            "Let's try an example: y equals 2 x squared minus 8 x plus 5. "
            "Here, a equals 2 and b equals negative 8. "
            "Plug them into x equals negative b over 2 a: negative of negative 8 is positive 8, divided by 2 times 2 which is 4. "
            "8 divided by 4 equals 2, so the axis of symmetry is x equals 2. "
            "Now let's try a practice problem: y equals negative 3 x squared minus 12 x plus 7. "
            "Here, a equals negative 3 and b equals negative 12. "
            "Negative b is positive 12, and 2 a is negative 6. "
            "12 divided by negative 6 gives x equals negative 2!"
        ),
        "steps": [
            ("Standard Form", r"y = 2x^2 - 8x + 5", "#0f172a"),
            ("Formula", r"x = -\frac{b}{2a}", "#2563eb"),
            ("Substitute", r"x = -\frac{-8}{2(2)} = \frac{8}{4}", "#059669"),
            ("Axis of Symmetry", r"x = 2", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"y = -3x^2 - 12x + 7", "#0f172a"),
            ("a = -3, b = -12", r"x = -\frac{-12}{2(-3)}", "#2563eb"),
            ("Answer", r"x = -2", "#059669"),
        ],
    },
    {
        "id": "expand_distributive",
        "title": "Expand by Distributive Property",
        "rule": r"(a + b)(c + d) = a(c + d) + b(c + d)",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are expanding binomials using the distributive property. "
            "Expanding converts a quadratic from factored form into standard form. "
            "Let's expand x plus 3 times x plus 5. "
            "Using the distributive property, multiply each term in the first bracket by the entire second bracket: "
            "x times x plus 5, plus 3 times x plus 5. "
            "Distribute x: x times x is x squared, and x times 5 is 5 x. "
            "Distribute 3: 3 times x is 3 x, and 3 times 5 is 15. "
            "Finally, combine the like terms in the middle: 5 x plus 3 x equals 8 x. "
            "So our expanded standard form is x squared plus 8 x plus 15. "
            "Now let's try a practice problem with a leading coefficient: expand 2 x minus 1 times x plus 4. "
            "Multiply 2 x by x plus 4 to get 2 x squared plus 8 x, then negative 1 by x plus 4 to get minus x minus 4. "
            "Combine 8 x minus x to get 2 x squared plus 7 x minus 4!"
        ),
        "steps": [
            ("Example 1", r"(x + 3)(x + 5)", "#0f172a"),
            ("Distribute", r"x(x + 5) + 3(x + 5)", "#2563eb"),
            ("Multiply", r"x^2 + 5x + 3x + 15", "#059669"),
            ("Standard Form", r"x^2 + 8x + 15", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"(2x - 1)(x + 4)", "#0f172a"),
            ("Multiply", r"2x^2 + 8x - x - 4", "#2563eb"),
            ("Answer", r"2x^2 + 7x - 4", "#059669"),
        ],
    },
    {
        "id": "expand_area_model",
        "title": "Expand Using an Area Model",
        "rule": r"\text{Total Area} = \sum \text{Region Areas}",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are expanding binomials visually using an area model. "
            "Think of multiplying two binomials as finding the total area of a rectangle split into four smaller boxes. "
            "Let's expand x plus 2 times x plus 4. "
            "Write x and positive 2 along the top, and x and positive 4 along the left side. "
            "Now multiply the row and column headers for each of the four regions: "
            "Top-left: x times x equals x squared. Top-right: x times 2 equals 2 x. "
            "Bottom-left: 4 times x equals 4 x. Bottom-right: 4 times 2 equals 8. "
            "Add all four areas together and combine the diagonal like terms 4 x plus 2 x to get x squared plus 6 x plus 8. "
            "Now let's try a practice problem: expand x plus 5 times x minus 3 using the area model. "
            "The four regions are x squared, 5 x, negative 3 x, and negative 15. "
            "Combine 5 x minus 3 x to get 2 x, giving x squared plus 2 x minus 15!"
        ),
        "steps": [
            ("Dimensions", r"(x + 2)(x + 4)", "#0f172a"),
            ("4 Area Regions", r"x^2,\quad 2x,\quad 4x,\quad 8", "#2563eb"),
            ("Sum Regions", r"x^2 + 2x + 4x + 8", "#059669"),
            ("Standard Form", r"x^2 + 6x + 8", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"(x + 5)(x - 3)", "#0f172a"),
            ("Regions", r"x^2 + 5x - 3x - 15", "#2563eb"),
            ("Answer", r"x^2 + 2x - 15", "#059669"),
        ],
    },
    {
        "id": "expand_special_product",
        "title": "Expand Special Products",
        "rule": r"(a + b)^2 = a^2 + 2ab + b^2",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are expanding special products, and avoiding the number-one algebra trap. "
            "When you see x plus 3 all squared, NEVER just square each term to get x squared plus 9! "
            "Squaring a binomial means multiplying it by itself: x plus 3 times x plus 3. "
            "Using the perfect square pattern, a plus b squared equals a squared plus 2 a b plus b squared. "
            "With a equals x and b equals 3, we get x squared plus 2 times x times 3 plus 3 squared, which simplifies to x squared plus 6 x plus 9. "
            "The second special product is sum and difference: a plus b times a minus b equals a squared minus b squared. "
            "Now let's try a practice problem: expand 2 x minus 5 all squared. "
            "Square the first term: 2 x squared is 4 x squared. "
            "Double the product: 2 times 2 x times negative 5 is negative 20 x. "
            "Square the last term: negative 5 squared is positive 25. So the answer is 4 x squared minus 20 x plus 25!"
        ),
        "steps": [
            ("Perfect Square", r"(x + 3)^2", "#0f172a"),
            ("Pattern", r"a^2 + 2ab + b^2", "#2563eb"),
            ("Substitute", r"x^2 + 2(x)(3) + 3^2", "#059669"),
            ("Expanded Form", r"x^2 + 6x + 9", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"(2x - 5)^2", "#0f172a"),
            ("a = 2x, b = -5", r"(2x)^2 + 2(2x)(-5) + (-5)^2", "#2563eb"),
            ("Answer", r"4x^2 - 20x + 25", "#059669"),
        ],
    },
    {
        "id": "discriminant_x_intercepts",
        "title": "Discriminant & x-Intercepts",
        "rule": r"D = b^2 - 4ac",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are determining the number of x-intercepts of a quadratic using the discriminant. "
            "The discriminant is the expression inside the square root of the quadratic formula: D equals b squared minus 4 a c. "
            "There are three cases. "
            "Case 1: if D is greater than 0, the square root is positive, giving 2 distinct real x-intercepts. "
            "Case 2: if D equals 0, plus or minus 0 gives the exact same value, so the vertex sits right on the x-axis with 1 x-intercept. "
            "Case 3: if D is less than 0, you cannot take the real square root of a negative number, so there are 0 real x-intercepts. "
            "Now let's test a practice problem: how many x-intercepts does y equals 2 x squared minus 4 x plus 5 have? "
            "Substitute a equals 2, b equals negative 4, and c equals 5 into b squared minus 4 a c. "
            "Negative 4 squared is 16, minus 4 times 2 times 5 which is 40. "
            "16 minus 40 is negative 24, which is less than 0—so there are 0 x-intercepts!"
        ),
        "steps": [
            ("Discriminant", r"D = b^2 - 4ac", "#0f172a"),
            ("D > 0", r"2 \text{ distinct x-intercepts}", "#059669"),
            ("D = 0", r"1 \text{ x-intercept (vertex on axis)}", "#2563eb"),
            ("D < 0", r"0 \text{ real x-intercepts}", "#dc2626"),
        ],
        "practice": [
            ("Try It Yourself", r"y = 2x^2 - 4x + 5", "#0f172a"),
            ("Compute D", r"D = (-4)^2 - 4(2)(5) = -24", "#2563eb"),
            ("Answer", r"D < 0 \implies 0 \text{ x-intercepts}", "#dc2626"),
        ],
    },
    {
        "id": "completing_the_square",
        "title": "Completing the Square",
        "rule": r"x^2 + bx = \left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are converting standard form to vertex form by completing the square. "
            "Let's convert y equals x squared plus 6 x plus 5 into vertex form. "
            "Step one: group the x squared and x terms together. "
            "Step two: take half of b, which is 6 divided by 2 equals 3, and square it to get 9. "
            "Step three: add and subtract 9 inside the brackets so the value of the equation stays unchanged. "
            "Step four: the first three terms, x squared plus 6 x plus 9, form a perfect square trinomial: x plus 3 all squared! "
            "Keep the negative 9 outside the bracket and combine it with plus 5: negative 9 plus 5 is negative 4. "
            "So vertex form is y equals x plus 3 squared minus 4, with vertex negative 3, negative 4. "
            "Now let's try a practice problem: complete the square for y equals x squared minus 8 x plus 10. "
            "Half of negative 8 is negative 4, squared is 16. "
            "Add and subtract 16: x minus 4 squared minus 16 plus 10, which gives x minus 4 squared minus 6!"
        ),
        "steps": [
            ("Standard Form", r"y = x^2 + 6x + 5", "#0f172a"),
            ("Half of 6, squared: 9", r"y = (x^2 + 6x + 9 - 9) + 5", "#2563eb"),
            ("Factor Trinomial", r"y = (x + 3)^2 - 9 + 5", "#059669"),
            ("Vertex Form", r"y = (x + 3)^2 - 4", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"y = x^2 - 8x + 10", "#0f172a"),
            ("Add & Sub 16", r"(x^2 - 8x + 16) - 16 + 10", "#2563eb"),
            ("Answer", r"y = (x - 4)^2 - 6", "#059669"),
        ],
    },
    {
        "id": "vertex_optimal_value",
        "title": "Vertex & Max/Min Optimal Value",
        "rule": r"a > 0 \implies \text{Min } k \quad | \quad a < 0 \implies \text{Max } k",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are finding the vertex and the maximum or minimum optimal value of a quadratic. "
            "In vertex form y equals a times x minus h squared plus k, the vertex is h, k. "
            "The y-coordinate k is the optimal value, and the x-coordinate h tells us where it occurs. "
            "If a is positive, the parabola opens upward like a U, so it has a minimum value. "
            "If a is negative, the parabola opens downward like an upside-down U, so it has a maximum value. "
            "Let's analyze y equals negative 2 times x minus 3 squared plus 8. "
            "The vertex is 3, 8. Since a equals negative 2 is less than 0, the parabola opens downward. "
            "Therefore, it has a maximum value of 8 when x equals 3. "
            "Now let's try a practice problem: find the optimal value of y equals 4 times x plus 1 squared minus 7. "
            "The vertex is negative 1, negative 7. Since a equals 4 is positive, it opens upward, "
            "so it has a minimum value of negative 7 when x equals negative 1!"
        ),
        "steps": [
            ("Vertex Form", r"y = -2(x - 3)^2 + 8", "#0f172a"),
            ("Vertex", r"V(3, 8)", "#2563eb"),
            ("Direction", r"a = -2 < 0 \implies \text{Opens Down}", "#059669"),
            ("Optimal Value", r"\text{Max } y = 8 \text{ at } x = 3", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"y = 4(x + 1)^2 - 7", "#0f172a"),
            ("a = 4 > 0, V(-1, -7)", r"\text{Opens Up}", "#2563eb"),
            ("Answer", r"\text{Min } y = -7 \text{ at } x = -1", "#059669"),
        ],
    },
    {
        "id": "equation_from_graph_vertex",
        "title": "Equation from Vertex & Point",
        "rule": r"\text{Sub } (h, k) \text{ and } (x, y) \text{ to solve for } a",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are finding the equation of a quadratic function given its vertex and one other point. "
            "Whenever you are given the vertex, always start with vertex form: y equals a times x minus h squared plus k. "
            "Let's find the equation of a parabola with vertex 2, negative 3 that passes through the point 4, 5. "
            "Step one: substitute h equals 2 and k equals negative 3 into vertex form: y equals a times x minus 2 squared minus 3. "
            "Step two: substitute the point x equals 4 and y equals 5: 5 equals a times 4 minus 2 squared minus 3. "
            "Step three: simplify and solve for a. 4 minus 2 is 2, and 2 squared is 4. Add 3 to both sides to get 8 equals 4 a, so a equals 2. "
            "Step four: write the final equation with a, h, and k filled in: y equals 2 times x minus 2 squared minus 3. "
            "Now try a practice problem: vertex 1, 4 passing through 3, negative 4. "
            "Plugging in gives negative 4 equals a times 3 minus 1 squared plus 4, so negative 8 equals 4 a, giving a equals negative 2!"
        ),
        "steps": [
            ("Vertex (2, -3)", r"y = a(x - 2)^2 - 3", "#0f172a"),
            ("Sub Point (4, 5)", r"5 = a(4 - 2)^2 - 3", "#2563eb"),
            ("Solve for a", r"8 = 4a \implies a = 2", "#059669"),
            ("Equation", r"y = 2(x - 2)^2 - 3", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"V(1, 4),\; P(3, -4)", "#0f172a"),
            ("Sub Point", r"-4 = a(3 - 1)^2 + 4", "#2563eb"),
            ("Answer", r"y = -2(x - 1)^2 + 4", "#059669"),
        ],
    },
    {
        "id": "graphing_step_pattern",
        "title": "Graphing with the Step Pattern",
        "rule": r"\text{Step Pattern} = a \times (1, 3, 5, \dots)",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are graphing quadratics super fast using the step pattern. "
            "For the parent parabola y equals x squared, every time you step 1 unit right from the vertex, you go up by 1, then 3, then 5, then 7. "
            "When there is a vertical stretch factor a, you simply multiply that basic 1, 3, 5 pattern by a! "
            "Let's graph y equals 2 times x minus 1 squared minus 3. "
            "Step one: plot the vertex at 1, negative 3. "
            "Step two: multiply the step pattern 1, 3, 5 by a equals 2, which gives 2, 6, 10. "
            "Step three: from the vertex, go right 1 and up 2 to plot 2, negative 1. Then go right 1 and up 6 to plot 3, 5. "
            "Mirror those same points across the axis of symmetry x equals 1 to the left side! "
            "Now try a practice problem: what is the step pattern for y equals negative 0.5 times x plus 2 squared plus 6? "
            "Multiply 1, 3, 5 by negative 0.5 to get negative 0.5, negative 1.5, negative 2.5—meaning you step down!"
        ),
        "steps": [
            ("Vertex Form", r"y = 2(x - 1)^2 - 3", "#0f172a"),
            ("Plot Vertex", r"V(1, -3)", "#2563eb"),
            ("Basic Pattern", r"1,\; 3,\; 5", "#059669"),
            ("Multiply by a = 2", r"2 \times (1, 3, 5) = (2, 6, 10)", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"y = -0.5(x + 2)^2 + 6", "#0f172a"),
            ("Vertex: (-2, 6)", r"-0.5 \times (1, 3, 5)", "#2563eb"),
            ("Step Pattern", r"(-0.5,\; -1.5,\; -2.5)", "#059669"),
        ],
    },
    {
        "id": "quadratic_word_problem_max_area",
        "title": "Max Area Optimization Problem",
        "rule": r"\text{Optimal } x = \frac{r + s}{2} \implies \text{Max Area}",
        "voiceover": (
            "Welcome to M P M 2 D! Today we are solving a classic quadratic optimization word problem: maximizing rectangular area. "
            "Suppose a farmer has 40 meters of fencing to build a rectangular pen against a barn wall, so only three sides need fencing. "
            "Let w be the width and l be the length. The fencing constraint is 2 w plus l equals 40, so l equals 40 minus 2 w. "
            "Area equals width times length, so A of w equals w times 40 minus 2 w. "
            "Notice this is already in factored form! Its zeros are w equals 0 and w equals 20. "
            "The maximum area occurs on the axis of symmetry halfway between the zeros: 0 plus 20 divided by 2 equals 10 meters. "
            "Plug w equals 10 back in: length is 40 minus 20 equals 20 meters, and the maximum area is 10 times 20 equals 200 square meters! "
            "Now try a practice problem: same setup with 60 meters of fencing. "
            "A of w equals w times 60 minus 2 w, with zeros at 0 and 30. "
            "Halfway is w equals 15, giving a maximum area of 15 times 30 equals 450 square meters!"
        ),
        "steps": [
            ("Constraint", r"2w + l = 40 \implies l = 40 - 2w", "#0f172a"),
            ("Area Function", r"A(w) = w(40 - 2w)", "#2563eb"),
            ("Zeros: 0 and 20", r"w_{\max} = \frac{0 + 20}{2} = 10", "#059669"),
            ("Max Area", r"A(10) = 10(20) = 200\text{ m}^2", "#d97706"),
        ],
        "practice": [
            ("Try It Yourself", r"60\text{ m fencing} \implies A(w) = w(60 - 2w)", "#0f172a"),
            ("Optimal Width", r"w_{\max} = \frac{0 + 30}{2} = 15\text{ m}", "#2563eb"),
            ("Max Area", r"A(15) = 450\text{ m}^2", "#059669"),
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
