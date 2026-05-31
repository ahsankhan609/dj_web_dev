from django.urls import NoReverseMatch, URLResolver, get_resolver, reverse


def app_navigation(request: object) -> dict[str, list[dict[str, str]]]:
    resolver = get_resolver()
    seen_namespaces: set[str] = set()
    app_links: list[dict[str, str]] = []

    for pattern in resolver.url_patterns:
        if not isinstance(pattern, URLResolver):
            continue

        namespace = pattern.namespace
        if not namespace or namespace in seen_namespaces:
            continue

        try:
            url = reverse(f'{namespace}:index')
        except NoReverseMatch:
            continue

        seen_namespaces.add(namespace)
        app_links.append({
            'name': namespace.replace('_', ' ').title(),
            'namespace': namespace,
            'url': url,
        })

    app_links.sort(key=lambda app: app['name'])
    return {'app_links': app_links}
