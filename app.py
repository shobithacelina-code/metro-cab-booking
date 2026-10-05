import streamlit as st
from datetime import date
import random

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="MetroGo | Metro + Cab Booking",
    page_icon="🚇",
    layout="centered"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
}

.block-container {
    max-width: 950px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ================= HERO ================= */

.hero {
    background: linear-gradient(135deg, #172554, #2563eb);
    padding: 38px 25px;
    border-radius: 22px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 8px 25px rgba(37, 99, 235, 0.20);
}

.hero h1 {
    font-size: 45px;
    font-weight: 800;
    margin: 0;
    color: white;
}

.hero p {
    font-size: 20px;
    margin: 10px 0;
    color: white;
}

.hero small {
    font-size: 14px;
    color: white;
    opacity: 0.9;
}

/* ================= SECTION HEADINGS ================= */

.section-title {
    font-size: 24px;
    font-weight: 750;
    margin-top: 28px;
    margin-bottom: 14px;
    color: #172554;
}

/* ================= ROUTE CARD ================= */

.route-card {
    background-color: white;
    border-radius: 18px;
    padding: 25px;
    margin-top: 15px;
    margin-bottom: 20px;
    border: 1px solid #e2e8f0;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

.station {
    font-size: 22px;
    font-weight: 700;
    color: #172554;
}

.arrow {
    color: #2563eb;
    font-size: 30px;
    padding: 0 15px;
}

/* ================= CONFIRMATION ================= */

.confirmation-card {
    background-color: white;
    border-radius: 20px;
    padding: 28px;
    margin-top: 25px;
    border: 1px solid #dbe3f0;
    box-shadow: 0 6px 20px rgba(0,0,0,0.07);
}

.confirmed-title {
    text-align: center;
    font-size: 28px;
    font-weight: 800;
    color: #166534;
    margin-bottom: 10px;
}

.booking-id {
    text-align: center;
    background-color: #f1f5f9;
    padding: 13px;
    border-radius: 12px;
    font-weight: 700;
    margin: 15px 0 25px 0;
    color: #334155;
}

/* ================= FARE ================= */

.fare-box {
    background-color: #ffffff;
    border-radius: 15px;
    padding: 20px;
    border: 1px solid #e2e8f0;
    margin-top: 15px;
}

.fare-row {
    display: flex;
    justify-content: space-between;
    padding: 13px 0;
    border-bottom: 1px solid #e2e8f0;
    font-size: 16px;
}

.fare-total {
    display: flex;
    justify-content: space-between;
    padding-top: 18px;
    font-size: 22px;
    font-weight: 800;
    color: #1d4ed8;
}

/* ================= TOTAL ================= */

.total-card {
    background-color: #eff6ff;
    border: 2px solid #2563eb;
    border-radius: 18px;
    padding: 24px;
    text-align: center;
    margin-top: 20px;
}

.total-label {
    font-size: 16px;
    color: #475569;
}

.total-price {
    font-size: 42px;
    font-weight: 800;
    color: #1d4ed8;
}

/* ================= INFO CARDS ================= */

.info-card {
    background-color: white;
    border-radius: 15px;
    padding: 18px;
    border: 1px solid #e2e8f0;
    text-align: center;
    margin-top: 15px;
}

.info-number {
    font-size: 25px;
    font-weight: 800;
    color: #2563eb;
}

.info-label {
    color: #64748b;
    font-size: 14px;
}

/* ================= FOOTER ================= */

.footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    margin-top: 45px;
    padding-top: 20px;
    border-top: 1px solid #e2e8f0;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO HEADER
# =========================================================

st.markdown("""
<div class="hero">
    <h1>🚇 MetroGo</h1>
    <p>Smart Metro + Cab Booking</p>
    <small>Plan your journey • Book your ride • Travel smarter</small>
</div>
""", unsafe_allow_html=True)


# =========================================================
# STATION DATA
# =========================================================

stations = [
    "JNTUH",
    "Miyapur",
    "KPHB",
    "Ameerpet",
    "SR Nagar",
    "Begumpet",
    "Secunderabad",
    "LB Nagar"
]


# =========================================================
# METRO FARE FUNCTION
# =========================================================

def calculate_metro_fare(from_station, to_station):

    from_index = stations.index(from_station)
    to_index = stations.index(to_station)

    distance = abs(from_index - to_index)

    if distance == 0:
        return 0, 0

    if distance <= 2:
        fare = 30

    elif distance <= 4:
        fare = 40

    elif distance <= 6:
        fare = 50

    else:
        fare = 60

    return fare, distance


# =========================================================
# CAB FARE FUNCTION
# =========================================================

def calculate_cab_fare(cab_type):

    cab_fares = {
        "🚗 Mini": 120,
        "🚘 Sedan": 150,
        "🚙 SUV": 220
    }

    return cab_fares[cab_type]


# =========================================================
# PASSENGER DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">👤 Passenger Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    name = st.text_input(
        "Full Name",
        placeholder="Enter your full name"
    )

with col2:

    travel_date = st.date_input(
        "Travel Date",
        min_value=date.today()
    )


# =========================================================
# METRO JOURNEY
# =========================================================

st.markdown(
    '<div class="section-title">🚇 Metro Journey</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    from_station = st.selectbox(
        "From Station",
        stations
    )

with col2:

    to_station = st.selectbox(
        "To Station",
        stations
    )

tickets = st.number_input(
    "Number of Tickets",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)


# =========================================================
# ROUTE PREVIEW
# =========================================================

if from_station != to_station:

    st.markdown(
        f"""
        <div class="route-card">

            <div class="station">
                🚉 {from_station}
                <span class="arrow">→</span>
                {to_station} 🚉
            </div>

            <p style="color:#64748b; margin-top:12px;">
                Selected Metro Route
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# CAB SERVICE
# =========================================================

st.markdown(
    '<div class="section-title">🚕 Cab Service</div>',
    unsafe_allow_html=True
)

need_cab = st.radio(
    "Would you like to book a cab?",
    ["No", "Yes"],
    horizontal=True
)

cab_type = None
cab_destination = ""

if need_cab == "Yes":

    col1, col2 = st.columns(2)

    with col1:

        cab_type = st.selectbox(
            "Cab Type",
            [
                "🚗 Mini",
                "🚘 Sedan",
                "🚙 SUV"
            ]
        )

    with col2:

        cab_destination = st.text_input(
            "Cab Drop Location",
            placeholder="Example: Hitech City"
        )


# =========================================================
# BOOKING BUTTON
# =========================================================

st.markdown("---")

generate_booking = st.button(
    "🎟️ Generate Booking",
    use_container_width=True,
    type="primary"
)


# =========================================================
# BOOKING PROCESS
# =========================================================

if generate_booking:

    # =====================================================
    # VALIDATION
    # =====================================================

    if name.strip() == "":

        st.error("⚠️ Please enter your name.")

    elif from_station == to_station:

        st.error(
            "⚠️ From Station and To Station cannot be the same."
        )

    elif need_cab == "Yes" and cab_destination.strip() == "":

        st.error(
            "⚠️ Please enter the cab drop location."
        )

    else:

        # =================================================
        # METRO FARE
        # =================================================

        metro_fare, distance = calculate_metro_fare(
            from_station,
            to_station
        )

        metro_total = metro_fare * tickets

        # =================================================
        # CAB FARE
        # =================================================

        if need_cab == "Yes":

            cab_fare = calculate_cab_fare(cab_type)

        else:

            cab_fare = 0

        # =================================================
        # FINAL TOTAL
        # =================================================

        final_total = metro_total + cab_fare

        # =================================================
        # BOOKING ID
        # =================================================

        booking_id = (
            "MCB-"
            + travel_date.strftime("%Y%m%d")
            + "-"
            + str(random.randint(1000, 9999))
        )

        # =================================================
        # SUCCESS
        # =================================================

        st.success(
            "🎉 Booking generated successfully!"
        )

        # =================================================
        # CONFIRMATION CARD
        # =================================================

        st.markdown(
            """
            <div class="confirmation-card">

                <div class="confirmed-title">
                    ✅ BOOKING CONFIRMED
                </div>

            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="booking-id">
                🎟️ Booking ID: {booking_id}
            </div>
            """,
            unsafe_allow_html=True
        )

        # =================================================
        # PASSENGER INFORMATION
        # =================================================

        col1, col2 = st.columns(2)

        with col1:

            st.write("**👤 Passenger**")
            st.write(name)

            st.write("**📅 Travel Date**")
            st.write(
                travel_date.strftime("%d %B %Y")
            )

        with col2:

            st.write("**🎫 Tickets**")
            st.write(tickets)

            st.write("**📍 Metro Distance**")
            st.write(f"{distance} station(s)")

        # =================================================
        # ROUTE
        # =================================================

        st.markdown(
            f"""
            <div class="route-card">

                <div class="station">
                    🚉 {from_station}
                    <span class="arrow">→</span>
                    {to_station} 🚉
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        # =================================================
        # JOURNEY INFORMATION
        # =================================================

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(
                f"""
                <div class="info-card">

                    <div class="info-number">
                        {distance}
                    </div>

                    <div class="info-label">
                        Stations
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
                <div class="info-card">

                    <div class="info-number">
                        {tickets}
                    </div>

                    <div class="info-label">
                        Ticket(s)
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:

            st.markdown(
                f"""
                <div class="info-card">

                    <div class="info-number">
                        ₹{metro_total}
                    </div>

                    <div class="info-label">
                        Metro Fare
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        # =================================================
        # FARE BREAKDOWN
        # =================================================

        st.subheader("💰 Fare Breakdown")

        st.markdown(
            '<div class="fare-box">',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="fare-row">
                <span>🚇 Metro ({tickets} ticket(s))</span>
                <strong>₹{metro_total}</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

        if need_cab == "Yes":

            st.markdown(
                f"""
                <div class="fare-row">
                    <span>{cab_type}</span>
                    <strong>₹{cab_fare}</strong>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                f"📍 **Cab Drop Location:** {cab_destination}"
            )

        else:

            st.markdown(
                """
                <div class="fare-row">
                    <span>🚕 Cab</span>
                    <strong>Not Required</strong>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            f"""
            <div class="fare-total">
                <span>Total</span>
                <span>₹{final_total}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        # =================================================
        # BIG TOTAL
        # =================================================

        st.markdown(
            f"""
            <div class="total-card">

                <div class="total-label">
                    TOTAL BOOKING AMOUNT
                </div>

                <div class="total-price">
                    ₹{final_total}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        # Close confirmation card
        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        # =================================================
        # DIGITAL TICKET
        # =================================================

        ticket_text = f"""
==================================================
                    METROGO
             METRO + CAB BOOKING
==================================================

                 BOOKING CONFIRMED

Booking ID: {booking_id}

Passenger:
{name}

Travel Date:
{travel_date.strftime("%d %B %Y")}

--------------------------------------------------

METRO JOURNEY

From Station:
{from_station}

To Station:
{to_station}

Number of Tickets:
{tickets}

Distance:
{distance} station(s)

Metro Fare:
₹{metro_total}

--------------------------------------------------

CAB SERVICE

"""

        if need_cab == "Yes":

            ticket_text += f"""
Cab Type:
{cab_type}

Cab Destination:
{cab_destination}

Cab Fare:
₹{cab_fare}
"""

        else:

            ticket_text += """
Cab:
Not Required
"""

        ticket_text += f"""
--------------------------------------------------

TOTAL AMOUNT:
₹{final_total}

==================================================

Thank you for choosing MetroGo! 🚇🚕

Have a safe journey.

==================================================
"""

        # =================================================
        # DOWNLOAD
        # =================================================

        st.download_button(
            label="📄 Download Digital Ticket",
            data=ticket_text,
            file_name=f"{booking_id}.txt",
            mime="text/plain",
            use_container_width=True
        )

        # =================================================
        # NEW BOOKING
        # =================================================

        if st.button(
            "🔄 Start New Booking",
            use_container_width=True
        ):

            st.rerun()


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        🚇 <b>MetroGo</b> — Smart Metro + Cab Booking<br><br>

        Built with Python & Streamlit<br>

        Academic Portfolio Project • 2026

    </div>
    """,
    unsafe_allow_html=True
)