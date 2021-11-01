<div>

    <h3>Recent Posts</h3>

    <ul>

    % for unit in units:
        <li>
            <a href="/unit/{{ units['id'] }}">{{ units['name'] }}</a>
        </li>
    % end

    </ul>

</div>
