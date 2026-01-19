from manim import *

lecturer_label = "LECTURER"
lecturer_name = "DR. NTALASHA"
group_members = {
    ("Bulaya Mwanaute", "20150307"),
    ("Isaac Zimba", "21166850"),
    ("Chali Ponshano", "22103639"),
    ("Isha Chilobwe", "21179447"),
    ("Wana Lenge", "22111795"),
    ("Nanetu E Mushongoma", "22102890"),
    ("Evelyn Chileshe", "22103266"),
    ("Londa Chitalu", "22112733"),
    ("Tiness Kamwela", "21166386"),
    ("Suwilanji Nakaluzwe", "22106664"),
    ("Jansen Shomo", "21167095"),
    ("Eidmal Shomo", "22110963"),
    ("Margaret Chapwasha", "20147003"),
    ("Eric Sakala", "22105408"),
    ("Shekina B Mulenga", "22998278"),
    ("Chalwe Silas", "22177295"),
}


def create_graph_layout():
    # 5 Node "House/Kite" Shape
    # A, B at top horizontal
    nodes = ["A", "B", "C", "D", "E"]
    edges = [
        ("A", "B"), ("A", "C"),
        ("B", "D"), ("B", "C"),  # Diagonal connection for interest
        ("C", "E"), ("D", "E")
    ]

    layout = {
        "A": [-2.5, 2, 0],
        "B": [2.5, 2, 0],
        "C": [-3, -0.5, 0],
        "D": [3, -0.5, 0],
        "E": [0, -2.5, 0]
    }
    return nodes, edges, layout


def create_routing_table(title_text, data, color=BLUE):
    """
    Creates a VGroup resembling a table.
    data: list of tuples ("Dest", "Next", "Hops")
    """
    table_group = VGroup()

    # Header
    header = Rectangle(width=3.5, height=0.6, color=color, fill_opacity=0.2)
    header_text = Text(title_text, font_size=20, color=color).move_to(header.get_center())

    table_group.add(header, header_text)

    # Rows
    row_height = 0.5
    for i, (dest, next_hop, metric) in enumerate(data):
        row_rect = Rectangle(width=3.5, height=row_height, color=color, stroke_opacity=0.5)
        # Align below header
        row_rect.next_to(header, DOWN, buff=0).shift(DOWN * i * row_height)

        # Text: Dest | Next | Metric
        row_str = f"{dest}   |   {next_hop}   |   {metric}"
        row_txt = Text(row_str, font_size=18).move_to(row_rect.get_center())

        # Tag the text with the destination so we can find it later
        row_txt.dest_id = dest

        table_group.add(row_rect, row_txt)

    return table_group


def intro_main_section(scene, text):
    title = Text(text, font_size=48, weight=BOLD)
    scene.play(FadeIn(title, shift=UP * 0.5))
    scene.wait(1.5)
    scene.play(title.animate.scale(0.8).to_edge(UP, buff=0.5))
    return title


def run_subsection(scene, title_text, content_function):
    sub_title = Text(title_text, font_size=36, color=BLUE_B)
    scene.play(FadeIn(sub_title))
    scene.wait(0.5)
    scene.play(sub_title.animate.scale(0.8).to_edge(DOWN, buff=0.5))

    content_group = content_function()

    scene.play(FadeOut(content_group), FadeOut(sub_title))
    scene.wait(0.5)


class CinematicIntro(Scene):
    def construct(self):
        # Background digital grid for depth
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={"stroke_opacity": 0.15}
        )
        self.add(grid)

        # Main Title with Gradient
        title = Text("ROUTING INFORMATION PROTOCOL", font_size=44, weight=BOLD)
        title.set_color_by_gradient(BLUE_C, WHITE)

        # Assignment Context
        subtitle = Text("CS 460: INTERNET TECHNOLOGIES", font_size=24, color=GRAY_A)
        subtitle.next_to(title, DOWN, buff=0.4)

        # Dramatic Entry: Write title and Fade in Subtitle
        self.play(Write(title), run_time=2.5, rate_func=rate_functions.slow_into)
        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.play(Indicate(title, scale_factor=1.05, color=BLUE_B))
        self.wait(1)

        # Lecturer Section
        lec_label = Text(lecturer_label, font_size=16, color=BLUE_B, weight=LIGHT).shift(DOWN * 2)
        lec_name = Text(lecturer_name, font_size=26).next_to(lec_label, DOWN, buff=0.2)
        lec_group = VGroup(lec_label, lec_name)

        self.play(FadeIn(lec_group, shift=UP * 0.5))
        self.wait(2)

        # Dramatic Transition Out (Expanding away)
        self.play(
            FadeOut(title, scale=1.3),
            FadeOut(subtitle, scale=1.3),
            FadeOut(lec_group, shift=DOWN),
            grid.animate.set_opacity(0),
            run_time=1.2
        )


class MovieEndCredits(Scene):
    def construct(self):
        # 1. "THE END" - Big Cinematic Text
        the_end = Text("THE END", font_size=72, weight=BOLD)
        self.play(Write(the_end), run_time=2)
        self.wait(1.5)

        # Shrink and move up to let the credits roll
        self.play(the_end.animate.scale(0.4).to_edge(UP, buff=0.8))

        # 2. Member Data (16 members)
        members = group_members

        # 3. Building the Scroll
        roll = VGroup()

        # Section Header
        prod_team = Text("PRODUCTION TEAM", font_size=22, color=BLUE_B, weight=BOLD)
        roll.add(prod_team)

        for name, sn in members:
            # Cinematic Style: Name is the focus, SN is metadata
            entry = VGroup(
                Text(name.upper(), font_size=28, weight=MEDIUM),
                Text(f"Student ID: {sn}", font_size=16, color=GRAY_B)
            ).arrange(DOWN, buff=0.1)
            roll.add(entry)

        # Special Thanks Section
        thanks_header = Text("SPECIAL THANKS", font_size=22, color=BLUE_B, weight=BOLD)
        thanks_lec = Text(lecturer_name, font_size=28)
        thanks_group = VGroup(thanks_header, thanks_lec).arrange(DOWN, buff=0.2)
        roll.add(thanks_group)

        # Final Footer
        footer = Text("© 2026 - CS 460 Group Project", font_size=14, color=GRAY_C)
        roll.add(footer)

        # Formatting the roll
        roll.arrange(DOWN, buff=1.4)  # Huge vertical gaps between names
        roll.next_to(the_end, DOWN, buff=5)  # Start well below the screen

        # 4. The Scrolling Animation
        # Calculation: move it the distance of the height of the roll + screen height
        # Total time 18s for 16 people is a nice, slow, readable speed
        total_scroll_dist = roll.height + 12

        self.play(
            roll.animate.shift(UP * total_scroll_dist),
            run_time=18,
            rate_func=linear  # Constant speed is key for credits!
        )

        self.play(FadeOut(the_end))
        self.wait(1)


class Scene1CoreMechanics(Scene):
    def construct(self):
        # --- Section 1: Introduction ---
        main_title = intro_main_section(self, "Core Mechanics")

        # --- Subsection 1.1: Hop Count ---
        run_subsection(
            self,
            "Hop Count as Metric",
            self.content_hop_count
        )

        # --- Subsection 1.2: 15 Hop Limit ---
        run_subsection(
            self,
            "15 Hop Limit",
            self.content_hop_limit
        )

        # --- Subsection 1.3: Periodic Updates ---
        run_subsection(
            self,
            "Periodic Updates",
            self.content_periodic_updates
        )

        # End of Section 1: Fade out main title
        self.play(FadeOut(main_title))
        self.wait(1)

    # ==========================================
    # CONTENT ANIMATIONS
    # ==========================================

    def content_hop_count(self):
        # 1. Setup Graph
        # Layout: A on left, Z on right, 3 paths in between
        nodes = ["A", "B", "C", "D", "E", "F", "G", "Z"]
        edges = [
            ("A", "B"), ("B", "Z"),  # Route 1 (2 hops)
            ("A", "C"), ("C", "D"), ("D", "Z"),  # Route 2 (3 hops)
            ("A", "E"), ("E", "F"), ("F", "G"), ("G", "Z")  # Route 3 (4 hops)
        ]

        layout = {
            "A": [-5, 0, 0],
            "Z": [1, 0, 0],
            # Top Path
            "B": [-2, 2, 0],
            # Middle Path
            "C": [-3, 0.5, 0], "D": [-1, 0.5, 0],
            # Bottom Path
            "E": [-3.5, -2, 0], "F": [-2, -2, 0], "G": [-0.5, -2, 0]
        }

        g = Graph(
            nodes, edges,
            layout=layout,
            labels=True,
            vertex_config={"radius": 0.3, "color": BLUE},
            edge_config={"stroke_width": 2, "stroke_opacity": 0.3, "color": GRAY}
        )

        # 2. Setup Descriptive Text Table (Right side)
        table_title = Text("Routing Table", font_size=24).move_to([4, 2, 0])
        underline = Line(start=[2.5, 1.8, 0], end=[5.5, 1.8, 0], stroke_width=1)

        # Container for the rows
        rows_group = VGroup()

        full_group = VGroup(g, table_title, underline, rows_group)
        self.play(Create(g), Write(table_title), Create(underline))

        # 3. Animate Routes
        routes = [
            # (Edges list), (Text Description), (Color)
            ([("A", "B"), ("B", "Z")], "A-B-Z : 2 Hops", YELLOW),
            ([("A", "C"), ("C", "D"), ("D", "Z")], "A-C-D-Z : 3 Hops", RED),
            ([("A", "E"), ("E", "F"), ("F", "G"), ("G", "Z")], "A-E-F-G-Z : 4 Hops", RED),
        ]

        prev_row = None

        for i, (path_edges, text_str, color) in enumerate(routes):
            # Text Row
            row_text = Text(text_str, font_size=20, color=color).move_to([4, 1.2 - (i * 0.6), 0])
            rows_group.add(row_text)

            # Highlight Edges
            active_edges = [g.edges[e] for e in path_edges]

            for e in active_edges:
                self.play(e.animate.set_stroke(width=6, opacity=1, color=color), run_time=0.65)

            self.play(Write(row_text), )
            # self.play(
            #     *[e.animate.set_stroke(width=6, opacity=1, color=color) for e in active_edges],
            #     Write(row_text),
            #     run_time=1.5
            # )
            self.wait(1)

            # Dim Edges back
            self.play(
                *[e.animate.set_stroke(width=2, opacity=0.3, color=GRAY) for e in active_edges],
                run_time=0.5
            )

        return full_group

    def content_hop_limit(self):
        # 1. Setup Center Node and concentric rings
        # Visualizing "Reachability" rather than a complex graph
        center_node = Dot(point=ORIGIN, color=GREEN, radius=0.2)
        center_label = Text("A", font_size=24).next_to(center_node, UP)

        # Create rings of dots to represent network depth
        layers = VGroup()
        layer_colors = [GREEN_B, TEAL, BLUE, PURPLE, GRAY]  # Last is unreachable

        radii = [0.9, 1.7, 2.5]

        for i, r in enumerate(radii):
            layer = VGroup()
            num_dots = 6 + (i * 4)
            for j in range(num_dots):
                angle = j * (2 * PI / num_dots)
                pos = [r * np.cos(angle), r * np.sin(angle), 0]
                dot = Dot(point=pos, radius=0.07, color=GRAY_E)  # Start dark

                # Draw faint line to center (abstract connection)
                line = Line(ORIGIN, pos, stroke_width=1, stroke_opacity=0.1)
                layer.add(VGroup(line, dot))
            layers.add(layer)

        full_group = VGroup(center_node, center_label, layers)

        # Shift up slightly to avoid hitting subtitle at bottom
        full_group.shift(UP * 0.5).to_edge(LEFT, buff=0.5)

        self.play(FadeIn(full_group))

        # 2. Animate Ripple (Reachability)

        # Layer 0 (Close neighbors)
        self.play(
            layers[0].animate.set_color(GREEN),
            run_time=1
        )
        label_1 = Text("Hops < 15", font_size=20, color=GREEN).next_to(full_group, buff=0.3)
        self.play(Write(label_1))

        # Layer 1 (Mid neighbors)
        self.play(
            layers[1].animate.set_color(TEAL),
            run_time=1
        )

        # Layer 2 (Too far)
        # We don't color them bright, we emphasize they are unreachable
        label_2 = Text("> 15 Hops = Infinity", font_size=20, color=RED).next_to(label_1, DOWN)

        self.play(
            layers[2].animate.set_color(RED_E),  # Dark Red
            Write(label_2)
        )

        # Flash the "unreachable" nodes
        self.play(Indicate(layers[2], color=RED))
        self.wait(1)
        self.play(
            FadeOut(label_1),
            FadeOut(label_2),
        )
        # full_group.add(label_1, label_2)
        return full_group

    def content_periodic_updates(self):
        # 1. Visual Setup
        router_a = Circle(radius=0.5, color=WHITE, fill_opacity=0).shift(LEFT * 3)
        label_a = Text("Router A", font_size=20).next_to(router_a, DOWN)

        router_b = Circle(radius=0.5, color=WHITE, fill_opacity=0).shift(RIGHT * 3)
        label_b = Text("Router B", font_size=20).next_to(router_b, DOWN)

        link = Line(router_a.get_right(), router_b.get_left(), color=GRAY)

        # Create a "Table" above Router A
        table_box = Rectangle(height=1.5, width=1.2, color=BLUE)
        table_lines = VGroup(*[
            Line(table_box.get_left() + UP * i * 0.3, table_box.get_right() + UP * i * 0.3, stroke_width=1)
            for i in range(-2, 3)
        ])
        table_a = VGroup(table_box, table_lines).next_to(router_a, UP)

        full_group = VGroup(router_a, label_a, router_b, label_b, link, table_a)

        self.play(Create(full_group))

        # 2. Timer Animation
        timer_text = Text("30s Timer", font_size=24, color=YELLOW).move_to(UP * 2)
        self.play(Write(timer_text))

        # Simulate timer countdown (clock wipe)
        timer_circle = Circle(radius=0.3, color=YELLOW).next_to(timer_text, RIGHT)
        timer_line = Line(timer_circle.get_center(), timer_circle.get_top())
        self.play(Create(timer_circle))
        self.play(Rotate(timer_line, angle=-2 * PI,
                         about_point=timer_circle.get_center(), run_time=1.5))

        # 3. Broadcast Animation
        # Copy table, shrink to "packet", move to B, expand
        packet = table_a.copy()
        packet.generate_target()
        packet.target.scale(0.2).set_color(YELLOW).move_to(router_a.get_center())

        self.play(MoveToTarget(packet))

        # Move across link
        self.play(packet.animate.move_to(router_b.get_center()), run_time=1.5)

        # Expand at B
        table_b = table_a.copy().next_to(router_b, UP)
        self.play(Transform(packet, table_b))

        info_text = Text("Full table broadcast!", font_size=24, color=YELLOW).next_to(link, UP)
        self.play(Write(info_text))

        self.wait(1)
        self.play(FadeOut(timer_text, timer_circle, packet, info_text, timer_line))

        return full_group


class Scene2BuildingNetworkMap(Scene):
    def construct(self):
        # --- Section 1 (Briefly summarized for context if running full sequence) ---
        # (Assuming you might run this standalone or strictly following previous context)
        # For this specific run, I will focus on rendering Section 2 as requested.

        main_title = intro_main_section(self, "Building the Network Map")

        # --- Subsection 2.1: Initialization ---
        # We return the graph state so we can pass it to the next section
        graph_group, node_positions, edge_list = self.run_subsection_return_content(
            "Neighbor Discovery",
            self.content_initialization
        )

        # --- Subsection 2.2: Table Exchange ---
        # We pass the previous graph state to maintain continuity
        run_subsection(
            self,
            "Routing Table Exchange",
            lambda: self.content_table_exchange(node_positions, edge_list)
        )

        # --- Subsection 2.3: Convergence ---
        run_subsection(
            self,
            "Convergence",
            lambda: self.content_convergence(node_positions, edge_list)
        )

        self.play(FadeOut(main_title))
        self.wait(1)

    # ==========================================
    # HELPER METHODS (Updated)
    # ==========================================

    def run_subsection(self, title_text, content_function):
        sub_title = Text(title_text, font_size=36, color=BLUE_B)
        self.play(FadeIn(sub_title))
        self.wait(0.5)
        self.play(sub_title.animate.scale(0.8).to_edge(DOWN, buff=0.5))

        content_group = content_function()

        self.play(FadeOut(content_group), FadeOut(sub_title))
        self.wait(0.5)

    def run_subsection_return_content(self, title_text, content_function):
        """
        Special helper for 2.1 because we want to persist the graph data
        for 2.2 and 2.3 to ensure visual consistency.
        """
        sub_title = Text(title_text, font_size=36, color=BLUE_B)
        self.play(FadeIn(sub_title))
        self.wait(0.5)
        self.play(sub_title.animate.scale(0.8).to_edge(DOWN, buff=0.5))

        # content_function must return (Group, Nodes, Edges)
        content_group, nodes, edges = content_function()

        self.play(FadeOut(content_group), FadeOut(sub_title))
        self.wait(0.5)
        return content_group, nodes, edges

    # ==========================================
    # CONTENT ANIMATIONS (SECTION 2)
    # ==========================================

    def content_initialization(self):
        nodes, edges, layout = create_graph_layout()

        # 1. Fade In Graph
        graph = Graph(
            nodes, edges, layout=layout, labels=True,
            vertex_config={"radius": 0.3, "color": BLUE},
            edge_config={"stroke_width": 2, "color": GRAY}
        ).to_edge(LEFT, )
        self.play(Create(graph))

        # 2. Show Table A (Right Side)
        # Initial State: neighbors unknown (infinity)
        initial_data = [
            ("B", "-", "∞"),
            ("C", "-", "∞"),
            ("D", "-", "∞"),
            ("E", "-", "∞")
        ]
        table_a = create_routing_table("Router A Table", initial_data).next_to(graph, RIGHT, 0.5)
        self.play(FadeIn(table_a))

        # 3. Discovery Animation
        # Highlight Neighbors of A (B and C)
        neighbors = ["B", "C"]

        # Highlight Edges
        active_edges = [graph.edges[("A", "B")], graph.edges[("A", "C")]]

        # Update Table Rows
        # Find the text objects for B and C rows
        rows_to_update = []
        for i, mobj in enumerate(table_a):
            if isinstance(mobj, Text) and hasattr(mobj, 'dest_id') and mobj.dest_id in neighbors:
                rows_to_update.append(mobj)

        # Animate Text Change
        new_texts = []
        for i, row_txt in enumerate(rows_to_update):
            new_str = f"{row_txt.dest_id}   |   Direct   |   1"
            new_txt = Text(new_str, font_size=18, color=YELLOW).move_to(row_txt.get_center())
            # new_texts.append(Transform(row_txt, new_txt))
            edge = active_edges[i]
            self.play(edge.animate.set_color(YELLOW).set_stroke(width=6))
            self.play(Transform(row_txt, new_txt))
            self.play(edge.animate.set_color(GRAY).set_stroke(width=2))
            self.wait()

        # self.play(*new_texts)
        self.wait(1)

        # Dim edges
        # self.play(*[e.animate.set_color(GRAY).set_stroke(width=2) for e in active_edges])

        full_group = VGroup(graph, table_a)
        return full_group, nodes, edges

    def content_table_exchange(self, node_list, edge_list):
        _, _, layout = create_graph_layout()

        # Recreate Graph
        graph = Graph(
            node_list, edge_list, layout=layout, labels=True,
            vertex_config={"radius": 0.3, "color": BLUE},
            edge_config={"stroke_width": 2, "color": GRAY}
        )

        # 1. Focus on A and B
        # Visual trick: Group everything, scale up, shift down so A/B are central
        # We dim C, D, E
        dim_nodes = [graph.vertices[n] for n in ["C", "D", "E"]]
        dim_edges = [edge for k, edge in graph.edges.items() if "C" in k or "D" in k or "E" in k]

        # Keep A-B edge bright
        ab_edge = graph.edges[("A", "B")]

        self.add(graph)
        self.play(
            graph.animate.scale(1.5).shift(DOWN * 2.5),
            *[n.animate.set_opacity(0.2) for n in dim_nodes],
            *[e.animate.set_opacity(0.1) for e in dim_edges],
            ab_edge.animate.set_opacity(1)
        )

        # 2. Show Tables Side by Side above B
        # Table A (Known: B=1, C=1, D=Inf, E=Inf)
        data_a = [("B", "Dir", "1"), ("C", "Dir", "1"), ("D", "-", "∞"), ("E", "-", "∞")]
        table_a = create_routing_table("Table A", data_a, color=BLUE)

        # Table B (Known: A=1, C=1, D=1 (connected), E=Inf)
        # Note: B is connected to D and C in our graph
        data_b = [
            ("A", "Dir", "1"),
            ("C", "-", "∞"),
            ("D", "Dir", "1"),
            ("E", "-", "∞")
        ]
        table_b = create_routing_table("Table B", data_b, color=RED)

        # Position Tables: A starts at A, moves to B
        table_a.scale(0.6).next_to(graph.vertices["A"], UP)
        table_b.scale(0.6).next_to(graph.vertices["B"], UP)

        self.play(FadeIn(table_a), FadeIn(table_b))

        info_text1 = Text("A sends updates to B", font_size=24, color=YELLOW).to_edge(UP, buff=2.0)
        self.play(Write(info_text1))

        # 3. Animate Exchange (A sends to B)
        # Create a copy of A, move it to B
        packet_a = table_a.copy()
        self.play(packet_a.animate.move_to(graph.vertices["A"].get_center()).scale(0.2))
        self.play(packet_a.animate.move_to(graph.vertices["B"].get_center()),
                  table_b.animate.shift(RIGHT * 1.5))
        self.play(packet_a.animate.move_to(table_b.get_left() + LEFT * 1.0).scale(5))  # Expand next to B

        self.play(FadeOut(info_text1))

        # Highlight C row in A (Source of info)
        row_c_packet_a = [m for m in packet_a if isinstance(m, Text) and getattr(m, 'dest_id', None) == "C"][0]
        indicator_box = SurroundingRectangle(row_c_packet_a, color=YELLOW)
        self.play(Create(indicator_box))

        update_text = Text("B learns route to C via A (1+1=2)", font_size=18, color=YELLOW).move_to(info_text1)
        self.play(Write(update_text))

        # Move indicator to B's table (Row C)
        row_c_b = [m for m in table_b if isinstance(m, Text) and getattr(m, 'dest_id', None) == "C"][0]
        target_indicator_box = SurroundingRectangle(row_c_b, color=YELLOW)
        self.play(ReplacementTransform(indicator_box, target_indicator_box))
        self.play(FadeOut(target_indicator_box, indicator_box))

        # Update B's text
        new_text_b = Text("C   |   Via A   |   2", font_size=14, color=YELLOW).move_to(row_c_b.get_center())
        self.play(Transform(row_c_b, new_text_b))

        self.wait(1.5)
        self.play(FadeOut(update_text))

        # Now Table A copy is left of Table B

        # 4. Update Logic Visualization
        # A knows C (Metric 1). B knows C (Metric 1 - direct). No update needed really.
        # BUT wait, in our graph B is connected to D. A is NOT.
        # So A needs to learn D from B? Or B learns something from A?
        # Let's flip it: B sends table to A.
        # B knows D (Metric 1). A has D = Infinity.

        info_text = Text("B sends updates to A...", font_size=24, color=YELLOW).to_edge(UP, buff=2.0)
        self.play(Write(info_text))

        # Fade out A's packet next to B and restore normal position of B's table
        self.play(
            table_b.animate.next_to(graph.vertices["B"], UP),
            FadeOut(packet_a)
        )

        self.wait(1.5)

        # Animate Exchange (B sends to A)
        # Create a copy of B, move it to A
        packet_b = table_b.copy()
        self.play(packet_b.animate.move_to(graph.vertices["B"].get_center()).scale(0.2))
        self.play(packet_b.animate.move_to(graph.vertices["A"].get_center()),
                  table_a.animate.next_to(graph.vertices["A"], UP).shift(LEFT * 1.5))
        self.play(packet_b.animate.move_to(table_a.get_right() + RIGHT * 1.0).scale(5))  # Expand next to A

        # Highlight D row in B (Source of info)
        row_d_b = [m for m in packet_b if isinstance(m, Text) and getattr(m, 'dest_id', None) == "D"][0]
        indicator_box = SurroundingRectangle(row_d_b, color=YELLOW)
        self.play(Create(indicator_box))

        # Move indicator to A's table (Row D)
        row_d_a = [m for m in table_a if isinstance(m, Text) and getattr(m, 'dest_id', None) == "D"][0]
        target_indicator_box = SurroundingRectangle(row_d_a, color=YELLOW.opacity(0))
        self.play(ReplacementTransform(indicator_box, target_indicator_box))
        self.play(FadeOut(target_indicator_box))

        # Update A's text
        new_text_a = Text("D   |   Via B   |   2", font_size=14, color=YELLOW).move_to(row_d_a.get_center())
        self.play(Transform(row_d_a, new_text_a))

        update_text = Text("A learns route to D via B (1+1=2)", font_size=20, color=YELLOW).next_to(info_text, DOWN)
        self.play(Write(update_text))
        self.wait(1.5)
        self.play(
            FadeOut(packet_b),
            table_a.animate.next_to(graph.vertices["A"], UP)
        )
        full_group = VGroup(graph, table_a, table_b, info_text, update_text)
        return full_group

    def content_convergence(self, node_list, edge_list):
        _, _, layout = create_graph_layout()

        # Recreate Graph
        graph = Graph(
            node_list, edge_list, layout=layout, labels=True,
            vertex_config={"radius": 0.3, "color": BLUE},
            edge_config={"stroke_width": 2, "color": GRAY}
        )

        # Start Zoomed out
        self.add(graph.to_edge(LEFT, 0.3))

        # Add visual "Chaos" - packets flying everywhere
        packets = VGroup()
        animations = []

        for edge_key, edge_mob in graph.edges.items():
            u, v = edge_key
            # Create two dots per edge (u->v and v->u)
            p1_at_u = Dot(radius=0.08, color=YELLOW).move_to(graph.vertices[u].get_center())
            p2_at_v = Dot(radius=0.08, color=YELLOW).move_to(graph.vertices[v].get_center())
            packets.add(p1_at_u, p2_at_v)

            # Animate back and forth
            # animations.append(MoveAlongPath(p1_at_u, edge_mob, run_time=2, rate_func=linear))
            # animations.append(MoveAlongPath(p2_at_v, edge_mob, run_time=2, rate_func=linear))
            animations.append(p1_at_u.animate.move_to(p2_at_v))
            animations.append(p2_at_v.animate.move_to(p1_at_u))

        desc_text = Text("Routing tables exchanged globally...", font_size=24).next_to(graph, RIGHT, 0.3)
        desc_text_2 = Text("Until Convergence is reached.", font_size=24, color=GREEN).next_to(desc_text, DOWN)

        self.play(Write(desc_text))

        # Loop the packet animation twice
        self.play(AnimationGroup(*animations, lag_ratio=0.1))
        self.play(AnimationGroup(*animations, lag_ratio=0.1))

        self.play(Write(desc_text_2))
        self.wait(1)

        full_group = VGroup(graph, packets, desc_text, desc_text_2)
        return full_group


class Scene3HandlingChanges(Scene):
    def construct(self):
        # Setup Main Title
        main_title = intro_main_section(self, "Section 3: Handling Changes")

        # Reuse positions from Section 2 for consistency
        nodes, edges, layout = create_graph_layout()

        # --- Subsection 3.1: Link Failure & Poisoning ---
        run_subsection(
            self,
            "Link Failure & Route Poisoning",
            lambda: self.content_link_failure(nodes, edges, layout)
        )

        # --- Subsection 3.2: Split Horizon ---
        run_subsection(
            self,
            "Split Horizon",
            lambda: self.content_split_horizon(nodes, edges, layout)
        )

        # --- Subsection 3.3: Re-Convergence ---
        run_subsection(
            self,
            "Re-Convergence",
            lambda: self.content_reconvergence(nodes, edges, layout)
        )

        self.play(FadeOut(main_title))
        self.wait(1)

    # ==========================================
    # DATA & UI HELPERS
    # ==========================================

    # ==========================================
    # CONTENT SECTIONS
    # ==========================================

    def content_link_failure(self, node_list, edge_list, layout):
        # g = Graph(node_list, edge_list, layout=layout, labels=True)
        nodes, edges, layout = create_graph_layout()

        # table_b = self.create_mini_table("B's Table", ["Dest D: 1"], color=RED).next_to(g.vertices["B"], UP)
        table_b_data = [
            ("A", "Direct", "1"),
            ["C", "Direct", "1"],
            ("D", "Direct", "1"),
            ("E", "Via C", "2")
        ]

        # 1. Fade In Graph
        graph = Graph(
            nodes, edges, layout=layout, labels=True,
            vertex_config={"radius": 0.3, "color": BLUE},
            edge_config={"stroke_width": 2, "color": GRAY}
        ).to_edge(LEFT, buff=0.5)
        table_b = create_routing_table("Router B Table", table_b_data).next_to(graph, RIGHT, 0.5)
        self.play(
            Create(graph),
            FadeIn(table_b)
        )

        # 1. Failure
        target_edge = graph.edges[("B", "D")]
        self.play(target_edge.animate.set_color(RED).set_stroke(width=8))
        self.wait(0.5)

        # "Shatter" effect: Fade out and show a cross
        # cross = Cross(target_edge, stroke_color=RED)
        # self.play(Create(cross))
        for _ in range(3):
            self.play(FadeOut(target_edge), run_time=0.2)
            self.play(FadeIn(target_edge), run_time=0.2)
        self.play(FadeOut(target_edge), )

        # 2. Poisoning at Router B

        poison_text = Text(
            "Router B detects that direct path to D\nis no longer accessible and updates\ndistance to 16",
            font_size=20, color=RED).next_to(graph.vertices["B"], RIGHT, buff=0.1).shift(UP * 0.2)
        self.play(Write(poison_text))
        self.wait(2)
        # Update B's table to 16
        # new_table_b = self.create_mini_table("B's Table", ["Dest D: 16"], color=YELLOW).move_to(table_b)
        # table_b_data[1][2] = 16
        # new_table_b = create_routing_table("Router B Table", table_b_data).next_to(graph, RIGHT, 0.5)

        rows_to_update = []
        for i, mobj in enumerate(table_b):
            if isinstance(mobj, Text) and hasattr(mobj, 'dest_id') and mobj.dest_id == "D":
                rows_to_update.append(mobj)

        # Animate Text Change
        for i, row_txt in enumerate(rows_to_update):
            new_str = f"{row_txt.dest_id}   |   Direct   |   16"
            new_txt = Text(new_str, font_size=18, color=YELLOW).move_to(row_txt.get_center())
            self.play(Transform(row_txt, new_txt))
            # self.play(edge.animate.set_color(GRAY).set_stroke(width=2))
            self.wait()
            break

        self.play(
            Indicate(table_b),
            FadeOut(poison_text)
        )

        # 3. Triggered Update

        packet1 = table_b.copy().scale(0.15)
        self.play(
            packet1.animate.scale(0.15),
            packet1.animate.move_to(graph.vertices["B"])
        )
        packet2 = packet1.copy()
        self.play(
            packet1.animate.move_to(graph.vertices["A"]),
            packet2.animate.move_to(graph.vertices["C"]),
            run_time=1)
        self.play(
            FadeOut(
                packet1,
                packet2
            )
        )

        msg = Text("Triggered routing update is sent", font_size=18, color=YELLOW).next_to(table_b, UP, buff=0.5)
        self.play(Write(msg))
        self.wait(1)

        graph.remove_edges(("B", "D"))

        return VGroup(graph, table_b, msg, packet1)

    def content_split_horizon(self, node_list, edge_list, layout):

        # nodes, edges, layout = create_graph_layout()
        #
        # # table_b = self.create_mini_table("B's Table", ["Dest D: 1"], color=RED).next_to(g.vertices["B"], UP)
        # table_b_data = [
        #     ("A", "Direct", "1"),
        #     ["C", "Direct", "1"],
        #     ("D", "Direct", "1"),
        #     ("E", "Via C", "2")
        # ]

        # 1. Fade In Graph
        graph = Graph(
            node_list, edge_list, layout=layout, labels=True,
            vertex_config={"radius": 0.3, "color": BLUE},
            edge_config={"stroke_width": 2, "color": GRAY}
        )
        # table_b = create_routing_table("Router B Table", table_b_data).next_to(graph, RIGHT, 0.5)
        # self.play(Create(graph), FadeIn(table_b))
        #
        # # 1. Failure
        # target_edge = graph.edges[("B", "D")]
        # self.play(target_edge.animate.set_color(RED).set_stroke(width=8))
        # self.wait(0.5)

        # We focus on A and B
        # g = Graph(node_list, edge_list, layout=layout, labels=True)
        # Remove the failed edge B-D visually
        graph.remove_edges(("B", "D"))
        self.play(Create(graph))

        # Logic Explanation
        # logic_text = Text("Split Horizon: Preventing Loops", font_size=24, color=BLUE).to_edge(UP, buff=1.5)
        # self.play(Write(logic_text))

        # A has a route to D learned from B
        table_a_data = [
            ("B", "Direct", "1"),
            ["C", "Direct", "1"],
            ("D", "Via B", "2"),
            ("E", "Via C", "2")
        ]
        table_a = (create_routing_table("Router A Table", table_a_data, color=BLUE)
                   .next_to(graph.vertices["A"], LEFT)
                   .scale(0.7))

        self.play(FadeIn(table_a))

        # Animation of A trying to "help" B
        # update_packet = table_a.copy().scale(0.2)
        # self.play(update_packet.animate.move_to(graph.vertices["A"]))
        arrow = Arrow(graph.vertices["A"].get_center(), graph.vertices["B"].get_center(), buff=0.5,
                      color=RED.opacity(128))

        self.play(GrowArrow(arrow))

        # The Big NO
        # no_sign = Cross(arrow, stroke_color=RED, stroke_width=10)
        no_sign = Text("x", color=RED, font_size=20).move_to(arrow)
        for _ in range(3):
            self.play(FadeOut(no_sign), run_time=0.2)
            self.play(FadeIn(no_sign), run_time=0.2)
        self.play(FadeOut(no_sign), run_time=0.2)

        reason = Text("Don't advertise D back to B,\nas B is the source of this route.",
                      font_size=18, color=RED).next_to(graph, UP, buff=0.1)
        self.play(Write(reason))
        self.wait(2)

        # graph.edges.pop(())
        self.remove(graph)

        return VGroup(graph, table_a, arrow, no_sign, reason)

    def content_reconvergence(self, node_list, edge_list, layout):
        # nodes, edges, layout = create_graph_layout()

        # 1. Fade In Graph
        # graph = Graph(
        #     nodes, edges, layout=layout, labels=True,
        #     vertex_config={"radius": 0.3, "color": BLUE},
        #     edge_config={"stroke_width": 2, "color": GRAY}
        # ).to_edge(LEFT, )
        graph = Graph(
            node_list, edge_list, layout=layout, labels=True,
            vertex_config={"radius": 0.3, "color": BLUE},
            edge_config={"stroke_width": 2, "color": GRAY}
        ).scale(0.8).to_edge(RIGHT, buff=0.6)

        # The Re-healing
        # graph = Graph(node_list, edge_list, layout=layout, labels=True)
        graph.remove_edges(("B", "D"))
        self.play(FadeIn(graph))

        info = Text("An alternative path from A to D must be found", font_size=20, color=GREEN).to_edge(UP, buff=1.5)
        self.play(FadeIn(info))
        self.wait(1.5)
        self.play(FadeOut(info))

        # Highlight the alternative: A -> C -> E -> D
        alt_path = [("A", "C"), ("C", "E"), ("E", "D")]

        # Show C sharing its table with A
        # table_c = self.create_mini_table("C's Table", ["D via E: 2"], color=GREEN).next_to(graph.vertices["C"], DOWN)

        table_c_data = [
            ("A", "Direct", "1"),
            ["B", "Direct", "1"],
            ("D", "Via E", "2"),
            ("E", "Direct", "1")
        ]
        table_c = create_routing_table("Router C Table", table_c_data, color=GREEN).next_to(graph.vertices["C"],
                                                                                            DOWN).scale(0.8)
        # Update A's table
        table_a_data_initial = [
            ("B", "Direct", "1"),
            ["C", "Direct", "1"],
            ("D", "Via B", "2"),
            ("E", "Via C", "2")
        ]
        table_a = create_routing_table("Router A Table", table_a_data_initial, color=BLUE).next_to(
            graph.vertices["A"], LEFT, buff=0.3).scale(0.8)

        self.play(FadeIn(table_c, table_a))

        # Move update from C to A
        packet_c = table_c.copy()
        self.play(
            packet_c.animate.scale(0.15).move_to(graph.vertices["C"])
        )
        # self.wait()
        self.play(
            packet_c.animate.move_to(graph.vertices["A"]),
            table_a.animate.next_to(table_a, LEFT)
        )
        self.play(
            # table_a.animate.next_to(table_a, LEFT),
            packet_c.animate.scale(6.66667).next_to(table_a, RIGHT)
        )

        #
        # info = Text("A path to D has been found through C", font_size=20, color=GREEN).to_edge(UP, buff=1.5)

        # Highlight D row in C (Source of info)
        row_d_packet_c = [m for m in packet_c if isinstance(m, Text) and getattr(m, 'dest_id', None) == "D"][0]
        indicator_box = SurroundingRectangle(row_d_packet_c, color=YELLOW)
        self.play(
            Create(indicator_box))

        info_text = Text("A learns route to D via C (2+1=3)", font_size=18, color=YELLOW).next_to(graph, UP)
        self.play(Write(info_text))

        # Move indicator to B's table (Row C)
        row_d_a = [m for m in table_a if isinstance(m, Text) and getattr(m, 'dest_id', None) == "D"][0]
        target_indicator_box = SurroundingRectangle(row_d_a, color=YELLOW)
        self.play(ReplacementTransform(indicator_box, target_indicator_box))

        # Update A's text
        new_text_a = Text("D   |   Via C   |   3", font_size=14, color=GREEN).move_to(row_d_a.get_center())
        self.play(Transform(row_d_a, new_text_a))

        self.play(FadeOut(target_indicator_box, indicator_box, info_text))

        self.play(FadeOut(packet_c))
        self.play(table_a.animate.next_to(graph.vertices["A"], LEFT))

        # table_a = create_routing_table("Router A Table", initial_data).next_to(graph, RIGHT, 0.5)
        success = Text("Network Re-Converged", font_size=20, color=YELLOW).next_to(graph, UP)

        # # Glow the new path
        for u, v in alt_path:
            if (u, v) not in graph.edges:
                u, v = v, u
            self.play(graph.edges[(u, v)].animate.set_color(GREEN).set_stroke(width=6), run_time=0.3)
            # self.play(graph.edges[(u, v)].animate.set_color(GREEN).set_stroke(width=6), run_time=0.3)

        self.play(Write(success))
        self.wait(2)

        return VGroup(graph, table_c, table_a, success)


class CombinedScene(CinematicIntro, Scene1CoreMechanics, Scene2BuildingNetworkMap, Scene3HandlingChanges,
                    MovieEndCredits):
    def construct(self) -> None:
        CinematicIntro.construct(self)
        self.wait()
        Scene1CoreMechanics.construct(self)
        self.wait()
        Scene2BuildingNetworkMap.construct(self)
        self.wait()
        Scene3HandlingChanges.construct(self)
        self.wait()
        MovieEndCredits.construct(self)
