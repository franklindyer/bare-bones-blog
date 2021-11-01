<div>

    <h3>Recent Posts</h3>

    <ul>

    % for lesson in unit:
        <li>
            <a href="/lesson/{{ lesson['id'] }}">{{ lesson['name'] }}</a>
        </li>
    % end

    </ul>

</div>
