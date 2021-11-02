<div>

    <h3>Lessons about "{{ unit['name'] }}"</h3>

    <ul>

    % for lesson in lessons:
        <li>
            <a href="/lesson/{{ lesson['id'] }}">{{ lesson['name'] }}</a>
        </li>
    % end

    </ul>

    % if subunits != []:
    <h3>Subunits of "{{ unit['name'] }}"</h3>

    <ul>

    % for subunit in subunits:
        <li>
            <a href="/unit/{{ subunit['id'] }}">{{ subunit['name'] }}</a>
        </li>
    % end

    </ul>
    % end

</div>

<br/>

<a href="/">Go home</a>
