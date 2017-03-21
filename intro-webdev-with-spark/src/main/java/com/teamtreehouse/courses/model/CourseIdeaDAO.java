package com.teamtreehouse.courses.model;

import java.util.List;

/**
 * Created by zerom_000 on 7/8/2016.
 *
 * DAO = data access object
 * used to get the data
 */
public interface CourseIdeaDAO {
    boolean add(CourseIdea idea);

    List<CourseIdea> findAll();

    CourseIdea findBySlug(String slug);
}
