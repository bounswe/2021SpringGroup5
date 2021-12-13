import { httpClient } from '../httpClient';

export function searchRequest(data) {
    return httpClient.post('/search', {
        status: "upcoming",
        search_query: data.searchQuery,
        sort_func: {
            isSortedByLocation: data.isSortedByLocation
        },
        filter_func: {
            location: {
                lat: data.position.lat,
                lng: data.position.lng,
                radius: data.radiusKm
            },
            sportType: data.sportType,
            date: {
                startDate: data.startDate,
                endDate: data.endDate
            },
            capacity: data.capacity
        }
    });
}