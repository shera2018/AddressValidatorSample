function mergeSuggestions(phoneticSuggestions, ngramSuggestions, editDistanceSuggestions) {
    // Prioritize phonetic suggestions by placing them first in the final array
    const finalSuggestions = [...phoneticSuggestions, ...ngramSuggestions, ...editDistanceSuggestions];

    return finalSuggestions;
} 