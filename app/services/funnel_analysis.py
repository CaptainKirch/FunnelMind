from collections import defaultdict

# Define your funnel steps (ordered)
FUNNEL_STEPS = ["/landing", "/signup", "/thankyou"]

def compute_funnel_stats(events):
    session_map = defaultdict(list)

    # Group events by session_id
    for event in events:
        session_map[event.session_id].append(event)

    # Track how many sessions hit each step
    step_counts = {step: 0 for step in FUNNEL_STEPS}

    for session_events in session_map.values():
        visited_urls = [e.url for e in sorted(session_events, key=lambda x: x.timestamp)]
