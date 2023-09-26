<div>

    <h3>Recent Posts</h3>

    <ul>

    % for entry in recent:
        <li>
            <a href="/post/{{ entry['id'] }}">{{ entry['name'] }}</a>
        </li>
    % end

    </ul>

</div>
