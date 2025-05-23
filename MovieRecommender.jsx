import React, { useState } from "react"; import { Card, CardContent } from "@/components/ui/card"; import { Button } from "@/components/ui/button"; import { Input } from "@/components/ui/input"; import { Checkbox } from "@/components/ui/checkbox";

const genresList = [ "Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller", "Animation", ];

const dummyRecommendations = { Action: [ { title: "Mad Max: Fury Road", image: "https://image.tmdb.org/t/p/w500/8tZYtuWezp8JbcsvHYO0O46tFbo.jpg" }, { title: "John Wick", image: "https://image.tmdb.org/t/p/w500/ziEuG1essDuWuC5lpWUaw1uXY2O.jpg" }, ], Comedy: [ { title: "The Hangover", image: "https://image.tmdb.org/t/p/w500/kfX8Ctin3fSZbdnjh6CXSNZUOVP.jpg" }, { title: "Superbad", image: "https://image.tmdb.org/t/p/w500/ek8e8txUyUwd2BNqj6lFEerJfbq.jpg" }, ], // Add more dummy data per genre... };

export default function MovieRecommender() { const [selectedGenres, setSelectedGenres] = useState([]); const [recommendations, setRecommendations] = useState([]);

const toggleGenre = (genre) => { setSelectedGenres((prev) => prev.includes(genre) ? prev.filter((g) => g !== genre) : [...prev, genre] ); };

const getRecommendations = () => { let result = []; selectedGenres.forEach((genre) => { if (dummyRecommendations[genre]) { result = [...result, ...dummyRecommendations[genre]]; } }); setRecommendations(result); };

return ( <div className="p-6 max-w-5xl mx-auto"> <h1 className="text-3xl font-bold mb-4 text-center">AI Movie Recommender</h1>

<div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
    {genresList.map((genre) => (
      <div key={genre} className="flex items-center space-x-2">
        <Checkbox id={genre} onCheckedChange={() => toggleGenre(genre)} />
        <label htmlFor={genre} className="text-sm font-medium">
          {genre}
        </label>
      </div>
    ))}
  </div>

  <Button onClick={getRecommendations} className="mb-6 w-full">
    Get Recommendations
  </Button>

  <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
    {recommendations.map((movie, idx) => (
      <Card key={idx} className="rounded-2xl shadow-md">
        <img src={movie.image} alt={movie.title} className="rounded-t-2xl h-60 w-full object-cover" />
        <CardContent className="p-4">
          <h2 className="text-xl font-semibold">{movie.title}</h2>
        </CardContent>
      </Card>
    ))}
  </div>
</div>

); }

    
