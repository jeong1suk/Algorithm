def solution(cacheSize, cities):
    cache = []
    hit, miss = 0, 0
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            hit += 1
            # print(f"hit 발생, city={city} 교체, cache={cache}")

        else:
            if cache and len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(city)
            miss += 1
            # print(f"miss 발생, city={city}, cache={cache}")
    return hit * 1 + miss * 5