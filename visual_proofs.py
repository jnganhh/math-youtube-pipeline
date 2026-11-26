"""Geometric proof builders. Each generator yields one animation per spoken beat."""

from manim import (
    AnimationGroup, ApplyMethod, Arc, Circle, DashedLine, Dot, FadeIn, FadeOut, Group, Indicate,
    Line, MathTex, PI, Polygon, Rectangle, Rotate, Scene, Succession, Transform,
    UP, DOWN, RIGHT, LEFT, VGroup, ValueTracker, always_redraw,
)
import numpy as np

from visual_proof_topics import FPS
INK = "#172533"
BLUE = "#a7d5fa"
TEAL = "#8bddca"
GOLD = "#ffd483"
PINK = "#f4b5bf"
WHITE = "#ffffff"


def point(x, y):
    return np.array([x, y, 0.0])


def box(x, y, w, h, fill=BLUE, opacity=1):
    """A rectangle located by its lower-left corner."""
    return Rectangle(width=w, height=h, stroke_color=INK, stroke_width=3,
                     fill_color=fill, fill_opacity=opacity).move_to(point(x+w/2, y+h/2))


def poly(*vertices, fill=BLUE, opacity=.65):
    return Polygon(*vertices, stroke_color=INK, stroke_width=3,
                   fill_color=fill, fill_opacity=opacity)


def stroke(a, b, **kwargs):
    return Line(a, b, color=INK, stroke_width=3, **kwargs)


def formula(tex, y=-2.12):
    label = MathTex(tex, color=INK, font_size=32)
    if label.width > 3.65:
        label.scale_to_fit_width(3.65)
    return label.move_to(point(0, y))


def diff_of_squares(scene):
    a, b = 2.25, .80
    x, y = -1.53, -.85
    d = a-b
    corner = box(x+d, y+d, b, b, PINK)
    lower = box(x, y, a, d)
    strip = box(x, y+d, d, b, TEAL)
    scene.add(lower, strip, corner)
    yield corner.animate.shift(.46*UP+.55*RIGHT)
    target = point(x+a+b/2, y+d/2)
    yield AnimationGroup(
        FadeOut(corner, shift=.30*UP),
        Succession(ApplyMethod(strip.shift, .72*UP), Rotate(strip, PI/2),
                   ApplyMethod(strip.set_x, target[0]), ApplyMethod(strip.move_to, target)),
    )
    yield AnimationGroup(
        Group(lower, strip).animate.shift(.32*UP),
        FadeIn(formula(r"a^2-b^2=(a+b)(a-b)")),
    )


def arithmetic_series(scene):
    n, unit = 4, .57
    origin = point(-1.14, -.75)
    stairs = VGroup(*(box(0, 0, unit, unit).move_to(origin+unit*point(i,j))
                      for j in range(n) for i in range(n-j)))
    scene.add(stairs)
    yield stairs.animate.shift(.70*DOWN)
    origin += .70*DOWN
    twin = stairs.copy().set_fill(TEAL)
    scene.add(twin)
    split = point(unit, 2.90)
    yield twin.animate.shift(split)
    # Reflected cell centres (i,j) -> (n-i,n-1-j) fill precisely the missing cells.
    pivot = origin + unit*point(n/2,(n-1)/2)
    yield AnimationGroup(
        Succession(Rotate(twin, PI), ApplyMethod(twin.move_to, 2*pivot-stairs.get_center())),
        FadeIn(formula(r"1+2+\cdots+n=\frac{n(n+1)}2")),
    )


def triangle_area_sine(scene):
    o, a, b = point(-1.31,-.65), point(.54,-.65), point(-.43,.98)
    foot = point(b[0], o[1])
    tri = poly(o,a,b)
    tri.rotate(-.20, about_point=o)
    scene.add(tri)
    base_label = formula("a").scale(.76).next_to((o+a)/2, DOWN, buff=.12)
    ob = stroke(o,b)
    side = formula("b").scale(.76).next_to(ob.get_center(), LEFT, buff=.16)
    angle = formula("C").scale(.68).move_to(o+point(.54,.19))
    yield AnimationGroup(Rotate(tri, .20, about_point=o), FadeIn(base_label),
                         FadeIn(side), FadeIn(angle))
    # The moving endpoint drops down the true perpendicular.
    drop = ValueTracker(.01)
    altitude = always_redraw(lambda: stroke(b, b+(foot-b)*drop.get_value()))
    marker = box(foot[0]-.14, foot[1], .14, .14, opacity=0)
    scene.add(altitude)
    caption = formula(r"h=b\sin C")
    yield AnimationGroup(drop.animate.set_value(1), FadeIn(marker), FadeIn(caption))
    mirrored = poly(o,a,b,fill=TEAL,opacity=.46)
    scene.add(mirrored)
    # A half-turn about AB's midpoint (the slanted side from a to b) doubles the area.
    yield AnimationGroup(Rotate(mirrored, PI, about_point=(a+b)/2),
                         Transform(caption, formula(r"A=\tfrac12 ab\sin C")))


def unit_circle_identity(scene):
    r = 1.36
    centre = point(0,.32)
    circle = Circle(radius=r, color=INK, stroke_width=3).move_to(centre)
    t = ValueTracker(.28)
    end = lambda: centre+r*point(np.cos(t.get_value()), np.sin(t.get_value()))
    foot = lambda: point(end()[0],centre[1])
    radius = always_redraw(lambda: stroke(centre,end()))
    dot = always_redraw(lambda: Dot(end(),radius=.065,color=INK))
    scene.add(circle, radius, dot, stroke(centre-r*RIGHT,centre+r*RIGHT))
    yield t.animate.set_value(.95)
    legs = always_redraw(lambda: poly(centre,foot(),end(),fill=TEAL,opacity=.65))
    cos_label = formula(r"\cos\theta").scale(.66)
    sin_label = formula(r"\sin\theta").scale(.66)
    cos_label.add_updater(lambda label: label.next_to((centre+foot())/2, DOWN, buff=.12))
    sin_label.add_updater(lambda label: label.next_to((foot()+end())/2, RIGHT, buff=.10))
    scene.add(legs, radius, dot, cos_label, sin_label)
    coordinates = formula(r"(\cos\theta,\sin\theta)")
    yield AnimationGroup(t.animate.set_value(.43), FadeIn(coordinates))
    sizes = formula(r"\cos^2\theta+\sin^2\theta=1")
    yield AnimationGroup(t.animate.set_value(.94), Transform(coordinates, sizes))


def circle_centre_angle(scene):
    r = 1.46
    centre = point(0,.24)
    on_circle = lambda t: centre+r*point(np.cos(t),np.sin(t))
    a, b = on_circle(40*PI/180), on_circle(140*PI/180)
    angle = ValueTracker(244*PI/180)
    p = lambda: on_circle(angle.get_value())
    other = lambda: 2*centre-p()
    chords = always_redraw(lambda: VGroup(stroke(a,p()),stroke(b,p()),
                                          Dot(p(),radius=.061,color=INK)))
    circle = Circle(radius=r,color=INK,stroke_width=3).move_to(centre)
    p_label = formula("P").scale(.66)
    p_label.add_updater(lambda label: label.next_to(p(), DOWN, buff=.12))
    scene.add(circle, chords, Dot(centre,radius=.052,color=INK),
              formula("A").scale(.66).next_to(a, RIGHT, buff=.14),
              formula("B").scale(.66).next_to(b, LEFT, buff=.14),
              formula("O").scale(.66).next_to(centre, DOWN, buff=.13), p_label)
    yield angle.animate.set_value(292*PI/180)
    # Signed arcs let the exterior-angle proof switch from addition to subtraction.
    def construction():
        pp, q = p(), other()
        polar = lambda v: np.arctan2(v[1],v[0])
        qa, qb, qq = polar(a-centre), polar(b-centre), polar(q-centre)
        pa, pb, pq = polar(a-pp), polar(b-pp), polar(q-pp)
        def mark(start, end, radius, at, color):
            return Arc(radius=radius, start_angle=start, angle=end-start,
                       arc_center=at, color=color, stroke_width=5)
        return VGroup(poly(centre,a,pp,fill=TEAL,opacity=.38),
                      poly(centre,pp,b,fill=GOLD,opacity=.38),
                      DashedLine(pp,q,color=INK,stroke_width=2.5),
                      mark(qa,qq,.31,centre,"#087e76"),
                      mark(qq,qb,.39,centre,"#a36512"),
                      mark(pa,pq,.41,pp,"#087e76"),
                      mark(pq,pb,.49,pp,"#a36512"))
    spokes = always_redraw(construction)
    scene.add(spokes,chords)
    yield angle.animate.set_value(254*PI/180)
    yield AnimationGroup(angle.animate.set_value(326*PI/180),
                         FadeIn(formula(r"\angle AOB=2\angle APB")))


def sum_of_odd_numbers(scene):
    u, x, y = .52, -1.04,-.89
    colors = [BLUE, TEAL, GOLD, PINK]
    def layer(n):
        return VGroup(*(box(x+i*u,y+j*u,u,u,colors[n])
                        for i in range(n+1) for j in range(n+1) if max(i,j)==n))
    scene.add(layer(0))
    previous = None
    for n, tex in [(1,r"1+3=2^2"),(2,r"1+3+5=3^2"),(3,r"1+3+\cdots+(2n-1)=n^2")]:
        g = layer(n)
        g.shift(.39*UP+.41*RIGHT)
        scene.add(g)
        label = formula(tex)
        caption = FadeIn(label) if previous is None else Transform(previous,label)
        if previous is None:
            previous = label
        yield AnimationGroup(g.animate.shift(-.39*UP-.41*RIGHT), caption)


def geometric_series_half(scene):
    side, x, y = 2.7, -1.35, -.99
    remainder = box(x,y,side,side,WHITE)
    scene.add(remainder)
    w = h = side
    colors = [BLUE, TEAL, GOLD, PINK, BLUE, TEAL]
    def split(i):
        nonlocal x,y,w,h
        if i % 2 == 0:
            w /= 2
            piece = box(x,y,w,h,colors[i])
            x += w
        else:
            h /= 2
            piece = box(x,y,w,h,colors[i])
            y += h
        piece.shift(.39*LEFT if i%2==0 else .35*DOWN)
        return AnimationGroup(Transform(remainder,box(x,y,w,h,WHITE)),
                              piece.animate.shift(.39*RIGHT if i%2==0 else .35*UP))
    yield split(0)
    yield Succession(split(1),split(2))
    yield AnimationGroup(Succession(split(3),split(4),split(5)),
                         FadeIn(formula(r"\frac12+\frac14+\frac18+\cdots=1")))


def derivative_x_squared(scene):
    x, y, side = -1.26,-.94,1.86
    dx = ValueTracker(.02)
    base = box(x,y,side,side)
    right = always_redraw(lambda: box(x+side,y,dx.get_value(),side,TEAL))
    top = always_redraw(lambda: box(x,y+side,side,dx.get_value(),TEAL))
    corner = always_redraw(lambda: box(x+side,y+side,dx.get_value(),dx.get_value(),GOLD))
    scene.add(base,right,top,corner)
    yield dx.animate.set_value(.64)
    caption = formula(r"\Delta A=2x\,dx+(dx)^2")
    yield AnimationGroup(dx.animate.set_value(.39), FadeIn(caption))
    yield AnimationGroup(dx.animate.set_value(.018),
                         Transform(caption,formula(r"\frac{\Delta A}{dx}=2x+dx\;\longrightarrow\;2x")))


def law_of_cosines(scene):
    # Triangle C at the origin in local coordinates. Its projection is signed in the identity.
    c, a = point(-.96,-.32), point(1.06,-.32)
    b = point(-.33,.94)
    tri = poly(c,a,b)
    scene.add(tri)
    def side_square(p,q):
        normal = point((q-p)[1],-(q-p)[0])
        return poly(p,q,q+normal,p+normal,fill=TEAL,opacity=.44)
    squares = []
    for p,q in ((c,a),(a,b),(b,c)):
        target = side_square(p,q)
        start = poly(p,q,q+.02*(target.get_vertices()[2]-q),
                     p+.02*(target.get_vertices()[3]-p),fill=TEAL,opacity=.44)
        squares.append((start,target))
        scene.add(start)
    # Scale the entire construction as one unit so side squares remain in frame.
    combined = Group(tri,*(target for _,target in squares))
    centre = combined.get_center()
    for obj in [tri,*(s for s,_ in squares),*(t for _,t in squares)]:
        obj.scale(.70,about_point=centre).shift(-centre+point(0,.46))
    # Apply the identical affine transform to the vertices.
    c,a,b = [.70*(p-centre)+point(0,.46) for p in (c,a,b)]
    inside = (c+a+b)/3
    labels = VGroup()
    for name, p, q in (("a",c,a), ("c",a,b), ("b",b,c)):
        midpoint = (p+q)/2
        # Place each side label just inside its edge, clear of the exterior squares.
        normal = point((p-q)[1],(q-p)[0])
        normal /= np.linalg.norm(normal)
        if np.dot(normal, inside-midpoint) < 0:
            normal *= -1
        labels.add(formula(name).scale(.64).move_to(midpoint+.16*normal))
    labels.add(formula("C").scale(.59).move_to(c+.29*(inside-c)/np.linalg.norm(inside-c)))
    scene.add(labels)
    yield AnimationGroup(*(Transform(s,t) for s,t in squares))
    foot = point(b[0],c[1])
    tracker = ValueTracker(.02)
    altitude = always_redraw(lambda: stroke(b,b+(foot-b)*tracker.get_value()))
    scene.add(altitude)
    caption = formula(r"c^2=(a-b\cos C)^2+(b\sin C)^2")
    yield AnimationGroup(*(FadeOut(s,shift=.20*DOWN) for s,_ in squares),
                         tracker.animate.set_value(1),FadeIn(caption))
    altitude.clear_updaters()
    right = poly(foot,a,b,fill=GOLD,opacity=.48)
    shift = .39*UP+.23*RIGHT
    scene.add(right)
    yield AnimationGroup(Group(right,tri,altitude,labels).animate.shift(shift),
                         Transform(caption,formula(r"c^2=a^2+b^2-2ab\cos C")))


def completing_the_square_morph(scene):
    x,y,s,w = -1.33,-.67,1.70,.56
    base = box(x,y,s,s)
    one = box(x+s,y,w,s,TEAL)
    two = box(x+s+w,y,w,s,TEAL)
    scene.add(base,one,two)
    yield two.animate.shift(.17*RIGHT)
    target = point(x+s/2,y-w/2)
    yield Succession(Rotate(two,PI/2), ApplyMethod(two.move_to, target))
    plug = box(x+s,y-w,w,w,GOLD).shift(.55*DOWN+.36*RIGHT)
    yield AnimationGroup(plug.animate.shift(.55*UP-.36*RIGHT),
                         FadeIn(formula(r"x^2+bx+\left(\frac b2\right)^2=\left(x+\frac b2\right)^2")))


BUILDERS = {builder.__name__: builder for builder in (
    diff_of_squares, arithmetic_series, triangle_area_sine, unit_circle_identity,
    circle_centre_angle, sum_of_odd_numbers, geometric_series_half,
    derivative_x_squared, law_of_cosines, completing_the_square_morph,
)}


class VisualProofScene(Scene):
    """Run a single uninterrupted animation beat for each quantized narration segment."""

    def construct(self):
        self.camera.background_color = WHITE
        frames = self.segment_frames
        if not frames or any(n < 1 for n in frames):
            raise ValueError("Every narration segment needs at least one frame")
        animations = BUILDERS[self.proof_id](self)
        for count in frames:
            animation = next(animations, None)
            if animation is None:
                raise ValueError(f"Missing visual beat in {self.proof_id}")
            # Cairo samples [0, run_time) in steps of 1/fps. Stay inside the final
            # frame interval to avoid float rounding adding or dropping a frame.
            self.play(animation, run_time=(count-.25)/FPS)
        if next(animations, None) is not None:
            raise ValueError(f"Unexpected visual beat in {self.proof_id}")
