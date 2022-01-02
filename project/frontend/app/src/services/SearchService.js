import { httpClient } from '../httpClient';

export function eventSearchRequest(data) {
    console.log({
        status: "upcoming",
        search_query: data.searchQuery,
        sort_func: {
            isSortedByLocation: data.isSortedByLocation
        },
        filter_func: {
            location: data.position ? {
                lat: data.position.lat,
                lng: data.position.lng,
                radius: data.radiusKm
            } : null,
            sportType: data.sportType,
            date: {
                startDate: data.startDate,
                endDate: data.endDate
            },
            capacity: data.capacity
        }
    });

    return httpClient.post('/search/search_event/', {
        status: "upcoming",
        search_query: data.searchQuery,
        sort_func: {
            isSortedByLocation: data.isSortedByLocation
        },
        filter_func: {
            location: data.position ? {
                lat: data.position.lat,
                lng: data.position.lng,
                radius: data.radiusKm
            } : null,
            sportType: data.sportType,
            date: {
                startDate: data.startDate,
                endDate: data.endDate
            },
            capacity: data.capacity
        }
    });
}

export function equipmentSearchRequest(data) {
    console.log({
        active: data.active,
        search_query: data.searchQuery,
        sort_func: {
            isSortedByLocation: data.isSortedByLocation
        },
        filter_func: {
            location: data.position ? {
                lat: data.position.lat,
                lng: data.position.lng,
                radius: data.radiusKm
            } : null,
            sportType: data.sportType,
            created_date: {
                startDate: data.startDate,
                endDate: data.endDate
            },
        }
    });

    return httpClient.post('/search/search_equipment/', {
        active: data.active,
        search_query: data.searchQuery,
        sort_func: {
            isSortedByLocation: data.isSortedByLocation
        },
        filter_func: {
            location: data.position ? {
                lat: data.position.lat,
                lng: data.position.lng,
                radius: data.radiusKm
            } : null,
            sportType: data.sportType,
            created_date: {
                startDate: data.startDate,
                endDate: data.endDate
            },
        }
    });
}