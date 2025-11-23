AI-Powered Movie Recommendation System

This project includes a hybrid recommendation engine that combines OpenAI’s language understanding with TMDB’s data accuracy to deliver high-quality movie and TV recommendations.

How It Works

1. AI-Based Semantic Recommendation

When a user opens a movie or TV show, the frontend sends a request to:

GET /api/v1/recommend/:title

The backend uses OpenAI to generate five recommended titles by analyzing:

movie name

genre

tone

plot characteristics

thematic similarities

AI is only responsible for returning movie names, ensuring recommendations feel natural and contextually relevant.

2. TMDB Data Lookup

Because AI cannot provide accurate poster paths or TMDB IDs, the frontend takes each AI-generated title and sends it to our custom search endpoint:

GET /api/v1/tmdb/search?query=<title>

This endpoint calls TMDB’s search API and returns a structured movie object containing:

TMDB ID

poster path

backdrop

release date

overview

media type

This guarantees all displayed data stays accurate and up-to-date.

3. Frontend Rendering

Each AI recommendation is rendered using a dedicated RecommendedCard component:

Displays poster image

Shows title

Click → navigates to /watch/:tmdbId

Horizontally scrollable carousel (same UX as “Similar Movies” section)

The scroll logic uses:

scrollBy({ left: sliderRef.current.offsetWidth, behavior: "smooth" })

to achieve a Netflix-style smooth navigation.

Why Use AI?

TMDB provides “similar” results based strictly on metadata.
AI recommendations consider deeper aspects:

story arcs

emotional tone

subgenre

vibe/style

character dynamics

This results in more human-like and meaningful recommendations.

Error Handling & Fail-Safe Logic

If AI suggests a title TMDB can’t find → card is skipped

No poster returned → fallback image used

Empty results → section is hidden

TMDB 401/429 errors handled gracefully

Summary

This system blends the strengths of both platforms:

AI TMDB
Understands story-level semantics Provides real metadata
Suggests creative similar titles Ensures data accuracy
Personalized, natural recommendations Stable poster paths & IDs

Together, they produce a smart, reliable, and visually accurate recommendation engine
