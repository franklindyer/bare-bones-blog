% include('tpl/header.tpl')

<div>

    <h3>List of units</h3>

    <ul>

    % for unit in units:
        <li>
            <a href="/unit/{{ unit['id'] }}">{{ unit['name'] }}</a>
        </li>
    % end

    </ul>

</div>
