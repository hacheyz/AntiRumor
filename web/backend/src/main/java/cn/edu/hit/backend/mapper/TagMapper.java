package cn.edu.hit.backend.mapper;

import cn.edu.hit.backend.pojo.Tag;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface TagMapper {

  @Select("select * from tag where name=#{name}")
  Tag findByTagName(String name);

  @Insert("insert into tag(name) values(#{name})")
  void add(String name);

  @Select("select * from tag")
  List<Tag> list();
}
